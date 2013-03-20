# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Channel(models.Model):
    name = models.CharField(_(u"Nome do Canal"), max_length=50)
    description = models.TextField(_(u"Descrição"), blank=True)
    slug = models.SlugField(_(u"Endereço"), max_length=50)

    class Meta:
        verbose_name = u"canal"
        verbose_name_plural = u"canais"
        db_table = "channel"

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ("core:details", (self.slug,))
