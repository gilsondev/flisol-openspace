# -*- coding: utf-8 -*-

import tagging

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
    video = models.URLField(_(u"URL do Vídeo"), verify_exists=False,
                            max_length=200)

    class Meta:
        verbose_name = u"canal"
        verbose_name_plural = u"canais"
        db_table = "channel"

    def __unicode__(self):
        return self.name

    def get_hashtags(self):
        """Retorna as hashtags separados por espaço"""
        return ' '.join(self.hashtags.values_list('name', flat=True))

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


tagging.register(Channel, tag_descriptor_attr='hashtags',
                 tagged_item_manager_attr='hashed')
