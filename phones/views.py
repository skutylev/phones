from django.views.generic import ListView, DetailView, UpdateView
from phones.models import Person, Unit, PositionInUnit
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q
from haystack.query import SearchQuerySet
from haystack.generic_views import SearchView
from braces.views import LoginRequiredMixin
from django.views.decorators.http import require_GET
import requests
from django.contrib.auth.models import User

class ListPhones(ListView):
    template_name = 'phones/phones.html'
    model = Person
    context_object_name = 'list'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(ListPhones, self).get_context_data(**kwargs)
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


def call(request):
    if request.method == 'get':
        opt = dict()
        opt['caller'] = '818'
        opt['callee'] = request.GET.get('phone')
        opt['login'] = 'DTF:0101571'
        opt['password'] = '522677072'
        # opt['caller'] = request.user.profile.get_phone()
        return requests.post('https://webcall.datafox.ru:8008/cgi-bin/app-callback.pl', caller='818', callee=request.GET.get('phone'), login='DTF:0101571', password='522677072')
