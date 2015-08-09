from django.conf.urls import include, url
from django.contrib import admin
from phones.views import LoginView, ListPhonesView, DetailPhoneView, PhoneSearchView



urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^login/', LoginView.as_view()),
    url(r'^phones/$', ListPhonesView.as_view()),
    url(r'^phones/(?P<slug>[-\w]+)/details/$', DetailPhoneView.as_view(), name="phone_details"),
    url(r'^search/$', include('haystack.urls')),
    url(r'^search/$', PhoneSearchView.as_view(), name='search'),
]
