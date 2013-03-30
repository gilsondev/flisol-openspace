from django.conf.urls import patterns, url

urlpatterns = patterns('openspace.core.views',
    url(r'^$', 'channel_list', name='list'),
    url(r'^canais/(?P<slug>[-\w]+)/$', 'channel_detail', name='details'),
)
