from django.views.generic import ListView, DetailView, UpdateView
from phones.models import Person, Unit, PositionInUnit
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q
from haystack.query import SearchQuerySet
from haystack.generic_views import SearchView
from braces.views import LoginRequiredMixin


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
    context_object_name = 'units'

    def get_context_data(self, **kwargs):
        context = super(ListUnits, self).get_context_data(**kwargs)
        return context


class DetailPhone(DetailView):
    template_name = 'phones/detail.html'
    model = Person
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super(DetailPhone, self).get_context_data(**kwargs)
        #subordinates = Person.objects.select_related('subordinates').all().get(id='')
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


# def search_person(request):
#     if request.method == 'POST':
#         search_text = request.POST['search_text']
#     else:
#         search_text = ' '
#     person = Person.objects.filter(last_name__contains = search_text)
#     return render_to_response('search/ajax_search.html', {'person': person})

def search_people(request):
    people = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))
    return render_to_response('search/ajax_search.html', {'people': people})


# class UnitSearchView(SearchView):
#     template_name = 'search/unit.html'
#     queryset = SearchQuerySet().all()
#     context_object_name = 'object_list'
