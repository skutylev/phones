from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from django.contrib.auth.models import User
import allauth
from django.contrib import auth
from django.http import HttpResponseRedirect, Http404

class LoginView(TemplateView):
    template_name = "accounts/login.html"

