from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.http import Http404, HttpResponse, HttpResponseRedirect
from allauth.exceptions import ImmediateHttpResponse


class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        email_domain = sociallogin.user.email.split('@')[1].lower()
        if not email_domain == 'mitht.ru':
            raise ImmediateHttpResponse(HttpResponseRedirect('/forbidden/'))
        else:
            pass


class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "/{username}/"
        return path.format(username=request.user.username)



