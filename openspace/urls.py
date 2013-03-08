from django.conf.urls import patterns, include, url
from django.conf import settings

from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('^canal-teste/$', 'openspace.core.views.channel_detail', name='channel_detail'),
    url(r'^$', direct_to_template, {'template': 'base.html'}, name='home'),

    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
