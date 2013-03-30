# -*- coding: utf-8 -*-

from django.test import TestCase

from openspace.core.models import Channel


class ChannelURLTest(TestCase):
    def setUp(self):
        self.channel = Channel.objects.create(
            name="Channel Test",
            description="Description",
            slug="channel-test"
        )

        self.resp = self.client.get(self.channel.get_absolute_url())

    def test_get(self):
        """Acessa um canal e retorna status 200"""
        self.assertEquals(self.resp.status_code, 200)

    def test_template(self):
        """Renderiza o template de detalhes do canal"""
        self.assertTemplateUsed(self.resp, 'core/channel_detail.html')


class ChannelModelTest(TestCase):
    def setUp(self):
        self.channel = Channel.objects.create(
            name="Channel Test",
            description="Description",
            slug="channel-test"
        )

    def test_create(self):
        """Cria o canal corretamente"""
        self.assertTrue(self.channel.pk)

    def test_unicode(self):
        """Retorna a representacao do objeto"""
        self.assertEquals(u"Channel Test", unicode(self.channel))

    def test_hashtags(self):
        """Insere as hashtags separado por espaços ou virgula"""
        self.channel.hashtags.add("hashtag", "test" "others")
        self.assertTrue(self.channel.hashtags)
