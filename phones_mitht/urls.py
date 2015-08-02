from django.conf.urls import include, url
from django.contrib import admin
from phones.views import LoginView

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^login/', LoginView.as_view(), name='login'),
]
