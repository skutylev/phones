from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView, DetailView, ListView, FormView
from django.contrib.auth.models import User
import allauth
from django.contrib import auth
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone
from django.template import RequestContext, Context
from phones.models import Person
import simplejson as json
from django.http import HttpResponse
from haystack.query import SearchQuerySet
from haystack.generic_views import SearchView

class LoginView(TemplateView):
    template_name = 'accounts/login.html'

class ListPhonesView(ListView):
    template_name = 'phones/index.html'
    model = Person

    def get_context_data(self, **kwargs):
        context = super(ListPhonesView, self).get_context_data(**kwargs)
        return context

class DetailPhoneView(DetailView):
    template_name = 'phones/detail.html'
    model = Person

    def get_context_data(self, **kwargs):
        context = super(DetailPhoneView, self).get_context_data(**kwargs)
        return context


class PhoneSearchView(SearchView):
    template_name = "search/search.html"

    def get_queryset(self):
        queryset = super(PhoneSearchView, self).get_queryset()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(PhoneSearchView, self).get_context_data(*args, **kwargs)
        return context

    def autocomplete(request):
        sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
        suggestions = [result.last_name for result in sqs]
        # Make sure you return a JSON object, not a bare list.
        # Otherwise, you could be vulnerable to an XSS attack.
        the_data = json.dumps({
            'results': suggestions
        })
        return HttpResponse(the_data, content_type='application/json')