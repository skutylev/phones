from django.conf.urls import patterns, url, include
from phones.views import ListPhones, DetailPhone, CreatePhone, UpdatePhone


urlpatterns = patterns('',
    url(r'^$', ListPhones.as_view(paginate_by=10), name='list'),
    url(r'^search/$', include('haystack.urls')),
    url(r'^add/$', CreatePhone.as_view(template_name='phones/add.html'), name='add'),
    url(r'^update$', UpdatePhone.as_view(template_name='phones/update.html'), name='update'),
    url(r'^(?P<slug>[-\w]+)/$', DetailPhone.as_view(), name='detail'),
)