from django.views.generic import ListView, DetailView, UpdateView
from phones.models import Person, Unit, PositionInUnit
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q
from haystack.query import SearchQuerySet
from haystack.generic_views import SearchView
from braces.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth.models import User
import json


class Main(ListView):
    template_name = 'phones/main.html'
    model = Person
    context_object_name = 'main'


class ListPhones(ListView):
    template_name = 'phones/phones.html'
    model = Person
    context_object_name = 'list'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(ListPhones, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            user = self.request.user
        else:
            user = '4'

        callee = PositionInUnit.objects.filter(person__user=user).values('phone__number').distinct()
        if len(callee) > 0:
            context['callee'] = callee[0].get('phone__number')
        else:
            context['callee'] = '000'
        return context

    # def get_queryset(self):
    #     queryset = Person.objects.select_related().filter(publish=True, positioninunit__is_main=True).values()
    #     return queryset


class ListUnits(DetailView):
    template_name = 'phones/units.html'
    model = Unit

    def get_context_data(self, **kwargs):
        context = super(ListUnits, self).get_context_data(**kwargs)
        context['person'] = Person.objects.filter(positioninunit__unit=self.get_object())
        return context


class DetailPhone(DetailView):
    template_name = 'phones/detail.html'
    model = Person

    def get_context_data(self, **kwargs):
        context = super(DetailPhone, self).get_context_data(**kwargs)
        # context['addresses'] = PositionInUnit.objects.select_related(
        #     'address__street__street',
        #     'address__building__building',
        #     'address__campus__campus',
        #     'address__office__office',
        # ).filter(person=self.get_object()).values_list(
        #     'address__street__street',
        #     'address__building__building',
        #     'address__campus__campus',
        #     'address__office__office',
        # )

        context['street'] = set(PositionInUnit.objects.select_related('address__street__street').filter(person=self.get_object()).values_list('address__street__street', flat=True).distinct())
        context['building'] = set(PositionInUnit.objects.select_related('address__building__building').filter(person=self.get_object()).values_list('address__building__building', flat=True).distinct())
        context['campus'] = set(PositionInUnit.objects.select_related('address__campus__campus').filter(person=self.get_object()).values_list('address__campus__campus', flat=True).distinct())
        context['office'] = set(PositionInUnit.objects.select_related('address__office__office').filter(person=self.get_object()).values_list('address__office__office', flat=True).distinct())
        context['subordinates'] = PositionInUnit.objects.filter(chief=self.get_object()).values('person__last_name', 'person__first_name', 'person__middle_name', 'person__slug')

        return context


class UpdatePhone(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'middle_name', 'birthday',
              'photo',  'degree', 'science_rank', 'work_hours']
    redirect_unauthenticated_users = True

    def get(self, request, **kwargs):
        self.object = Person.objects.get(slug=self.kwargs['slug'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = Person.objects.get(slug=self.kwargs['slug'])
        return obj


def call(request, phone):
        opt = dict()
        opt['callee'] = phone
        opt['login'] = 'DTF:0101571'
        opt['password'] = '522677072'
        opt['caller'] = PositionInUnit.objects.filter(person__user=request.user).values_list('phone__number').distinct()[0][0]
        r = requests.post('https://webcall.datafox.ru:8008/cgi-bin/app-callback.pl', data=opt, verify=False,)
        html = "<html><body>Calling to number %s</body></html>" % phone
        return HttpResponse(html)


def autocomplete(request):
    if request.GET.get('q', '') == '':
        array = []
    else:
        array = []
        sqs = SearchQuerySet().autocomplete(last_name_auto=request.GET.get('q', '')).order_by('last_name')
        print(sqs.count())
        for result in sqs:
            data = {"tokens": str(result.last_name).split(),
                    "last_name": str(result.last_name),
                    "first_name": str(result.first_name[0]),
                    "middle_name": str(result.middle_name[0]),
                    "slug": str(result.slug),
                    "phone": str(result.phone)
                    }
            array.insert(0, data)
        print(array)
    return HttpResponse(json.dumps(array), content_type='application/json')

def autocomplete_unit(request):
    if request.GET.get('q', '') == '':
        array = []
    else:
        array = []
        sqs = SearchQuerySet().autocomplete(unit_name_auto=request.GET.get('q', '')).order_by('unit_name')
        print(sqs.count())
        for result in sqs:
            data = {"tokens": str(result.unit_name).split(),
                    "unit_name": str(result.unit_name),
                    "unit_short_name": str(result.unit_short_name),
                    "slug": str(result.slug)
                    }
            array.insert(0, data)
        print(array)
    return HttpResponse(json.dumps(array), content_type='application/json')