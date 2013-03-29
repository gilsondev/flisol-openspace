# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Channel(models.Model):
    name = models.CharField(_(u"Nome do Canal"), max_length=50)
    description = models.TextField(_(u"Descrição"), blank=True)
    slug = models.SlugField(_(u"Endereço"), max_length=50,
                            help_text=_(u"""
                                        Será a URL do seu canal.
                                        Exemplo:
                                        <strong>http://openspace.flisol.net/canais/
                                        [seu endereço]</strong>"""))

    class Meta:
        verbose_name = u"canal"
        verbose_name_plural = u"canais"
        db_table = "channel"

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ("core:details", (self.slug,))


# TODO: Inserir testes
class Programming(models.Model):
    text = models.TextField(u"Conteúdo da Programação")

    class Meta:
        verbose_name = u"programação"
        verbose_name_plural = u"programações"
        db_table = "programming"
