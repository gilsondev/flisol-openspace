# -*- coding: utf-8 -*-

from django import forms

from openspace.core.models import Channel


class ChannelForm(forms.ModelForm):
    hashtags = forms.CharField(
        label=u'Hashtags',
        help_text=u"""Separe por vírgula.
        <strong>Ex.: flisol, flisoldf</strong>""",
        widget=forms.TextInput(attrs={'class': 'vTextField'}))

    class Meta:
        model = Channel

    def __init__(self, *args, **kwargs):
        super(ChannelForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        channel = super(ChannelForm, self).save(commit=False)

        if commit:
            channel.save()
            if channel.hashtags:
                channel.hashtags.delete()
            channel.hashtags = self.cleaned_data['hashtags']

        return channel
