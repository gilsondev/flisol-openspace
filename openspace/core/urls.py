from django.conf.urls import patterns, url

urlpatterns = patterns('openspace.core.views',
    url('^(?P<slug>.*)$', 'channel_detail', name='details'),
)
