from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from phones.views import ListPhones, DetailPhone, CreatePhone, UpdatePhone, ListUnits

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^pubs/', include('pubs.urls'), name='pubs'),
    url(r'^$', ListPhones.as_view(), name='list'),
    url(r'^units', ListUnits.as_view(), name='units'),
    url(r'^search/$', include('haystack.urls')),
    url(r'^add/$', CreatePhone.as_view(template_name='phones/add.html'), name='add'),
    url(r'^update$', UpdatePhone.as_view(template_name='phones/update.html'), name='update'),
    url(r'^(?P<slug>[-\w]+)/$', DetailPhone.as_view(), name='detail'),
    url(r'^publications/', include('publications.urls')),
    url(r'^select2/', include('django_select2.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )