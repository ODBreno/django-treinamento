from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r

class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Breno Dias', cpf='12345678901',
                    email = 'breno.dias@kmee.com.br', phone='21-99618-6180')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)
    
    def test_subscription_email_from(self):
        expect = 'breno.dias@kmee.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['breno.dias@kmee.com.br', 'breno.dias@kmee.com.br']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Breno Dias',
            '12345678901', 
            'breno.dias@kmee.com.br',
            '21-99618-6180'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)