from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from phones.views import ListPhones, DetailPhone, UpdatePhone, ListUnits, call, autocomplete, autocomplete_unit, Main

# from phones.views import UnitSearchView

urlpatterns = patterns('',
    url(r'^$', Main.as_view(), name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^pubs/', include('pubs.urls'), name='pubs'),
    url(r'^all/$', ListPhones.as_view(), name='list'),
    # url(r'^units/$', ListUnits.as_view(), name='units'),
    url(r'^units/(?P<slug>[-\w]+)/$', ListUnits.as_view(), name='units'),
    url(r'^search/$', include('haystack.urls')),
    url(r'^search/autocomplete/$', autocomplete),
    url(r'^search/autocomplete/unit/$', autocomplete_unit),
    url(r'^(?P<slug>[-\w]+)/edit/$', UpdatePhone.as_view(template_name='phones/update.html'), name='edit'),
    url(r'^(?P<slug>[-\w]+)/$', DetailPhone.as_view(), name='detail'),
    url(r'^publications/', include('publications.urls')),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^call/(?P<phone>[-\d]+)/$', call),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )