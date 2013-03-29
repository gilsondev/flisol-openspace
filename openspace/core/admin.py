# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings

from openspace.core.models import Channel, Programming


class ChannelAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description')
    prepopulated_fields = {"slug": ("name",)}

    class Media:
        js = settings.TINY_MCE_FILES


class ProgrammingAdmin(admin.ModelAdmin):
    pass

    class Media:
        js = settings.TINY_MCE_FILES

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Programming, ProgrammingAdmin)
