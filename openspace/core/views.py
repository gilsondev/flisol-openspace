# -*- coding: utf-8 -*-

from django.shortcuts import render


def channel_detail(request):
    return render(request, 'core/channel_detail.html')
