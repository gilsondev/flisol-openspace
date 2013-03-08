# -*- coding: utf-8 -*-

from django.contrib import admin

from openspace.core.models import Channel


class ChannelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Channel, ChannelAdmin)
