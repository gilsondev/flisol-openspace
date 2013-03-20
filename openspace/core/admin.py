# -*- coding: utf-8 -*-

from django.contrib import admin

from openspace.core.models import Channel


class ChannelAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Channel, ChannelAdmin)
