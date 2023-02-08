from django.test import TestCase
from django.shortcuts import resolve_url as r
# Create your tests here.


class HomeTest(TestCase):
    fixtures=['keynotes.json']

    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)
    
    def test_speakers(self):
        contents = [
            'href="{}"'.format(r('speaker_detail', slug='grace-hopper')),
            'Grace Hopper',
            'https://minasyenergia.upm.es/images/thumbnails/images/Espacio_Igualdad/Exposicion_mujeres_ciencias/gracehopp-fill-172x226.jpg',
            'href="{}"'.format(r('speaker_detail', slug='alan-turing')),
            'Alan Turing',
            'https://cdn.britannica.com/81/191581-050-8C0A8CD3/Alan-Turing.jpg',
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)
    
    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)

    def test_talks_link(self):
        expected = 'href="{}"'.format(r('talk_list'))
        self.assertContains(self.response, expected)