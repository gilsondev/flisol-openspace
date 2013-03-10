# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from openspace.core.models import Channel


def channel_detail(request, slug):
    channel = get_object_or_404(Channel, slug=slug)
    return render(request, 'core/channel_detail.html', {'channel': channel})
