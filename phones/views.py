from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, DeleteView, DetailView, ListView, FormView
from django.contrib.auth.models import User
import allauth
from django.contrib import auth
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone
from django.template import RequestContext, Context
from phones.models import Person

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
