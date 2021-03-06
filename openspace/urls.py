# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('openspace.core.urls', namespace='core')),

    # Other Apps
    url(r'', include('social_auth.urls')),
    url(r'^grappelli/', include('grappelli.urls')),

    # Sobrescrevendo logout, pelo motivo do mesmo estar redirecionando
    # para o django admin. Vai ter o logout padrão, e vai ter para os
    # os usuários normais.
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout_user'),

    # Django Auth
    url(r'', include('django.contrib.auth.urls')),

    # Django Admin
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve', {
        'document_root': settings.STATIC_ROOT,
        'insecure': True}),
)
