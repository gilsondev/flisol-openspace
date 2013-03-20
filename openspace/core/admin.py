# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings

from openspace.core.models import Channel


class ChannelAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description')
    prepopulated_fields = {"slug": ("name",)}

    class Media:
        js = settings.TINY_MCE_FILES

admin.site.register(Channel, ChannelAdmin)
