from django.views.generic import ListView, DetailView, CreateView, UpdateView
from phones.models import Person
from django.core import paginator

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
