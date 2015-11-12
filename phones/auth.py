from django.dispatch import receiver
from allauth.socialaccount.signals import pre_social_login, social_account_added
from django.http import Http404
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        email_domain = sociallogin.user.email.split('@')[1].lower()
        if not email_domain == 'mitht.ru' or 'mitht.org':
                raise Http404
        else:
            pass



# @receiver(pre_social_login)
# def check_domain(sender, **kwargs):
#     """
#     signal: Sent after a user successfully authenticates via a social provider, but before the login is fully processed.
#             This signal is emitted as part of the social login and/or signup process, as well as when connecting additional social accounts to an existing account.
#             Access tokens and profile information, if applicable for the provider, is provided.
#     method: Receive pre_social_login signal and check social user e-mail domain by reg exp.
#
#     """
#
#
#
# @receiver(social_account_added)
# def link_to_contact(sender, **kwargs):
#     """
#     signal: Sent after a user connects a social account to a their local account.
#     method: Receive social_accound_added signal and connect authenticated user with person model compare e-mail
#     """
#     user = kwargs.pop('user')
#     user.save
#
