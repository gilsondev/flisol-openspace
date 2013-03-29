# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from openspace.core.models import Channel, Programming


# TODO: Ver uma melhor forma para disponibilizar a programação
def channel_detail(request, slug):
    channel = get_object_or_404(Channel, slug=slug)

    # TODO: É só para quebrar o galho. Sem tempo para fazer direito =/
    if Programming.objects.exists():
        programming = Programming.objects.all()[0]
    else:
        programming = ''
    return render(request, 'core/channel_detail.html',
                  {'channel': channel,
                   'programming': programming})
