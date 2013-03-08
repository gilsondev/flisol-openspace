# -*- coding: utf-8 -*-

from django.test import TestCase


class ChannelURLTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/canal-teste')

    def test_get(self):
        """Acessa um canal e retorna status 200"""
        self.assertEquals(self.resp.status_code, 200)

    def test_template(self):
        """Renderiza o template de detalhes do canal"""
        self.assertTemplateUsed(self.resp, 'core/channel_detail.html')
