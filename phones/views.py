from django.views.generic import ListView, DetailView, CreateView, UpdateView
from phones.models import Person
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q
from haystack.query import SearchQuerySet


from django.contrib.auth.models import User

class ListPhones(ListView):
    template_name = 'phones/phones.html'
    model = Person
    context_object_name = 'list'
    def get_context_data(self, **kwargs):
        context = super(ListPhones, self).get_context_data(**kwargs)
        return context


class DetailPhone(DetailView):
    template_name = 'phones/detail.html'
    model = Person
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super(DetailPhone, self).get_context_data(**kwargs)
        #subordinates = Person.objects.select_related('subordinates').all().get(id='')
        return context


class CreatePhone(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'middle_name', 'birthday',
              'email', 'photo', 'unit', 'position', 'degree', 'science_rank',
              'address', 'phone', 'work_hours']


class UpdatePhone(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'middle_name', 'birthday',
              'email', 'photo', 'unit', 'position', 'degree', 'science_rank',
              'address', 'phone', 'work_hours']


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