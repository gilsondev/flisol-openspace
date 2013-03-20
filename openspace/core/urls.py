from django.conf.urls import patterns, url

urlpatterns = patterns('openspace.core.views',
    url('^(?P<slug>[-\w+])/$', 'channel_detail', name='details'),
)
