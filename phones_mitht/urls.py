from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^phones/', include('phones.url'), name='phones'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
