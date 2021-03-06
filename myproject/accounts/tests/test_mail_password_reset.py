from django.core import mail
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

class PasswordResetMailTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', email='952775347@qq.com', password='123')
        self.response = self.client.post(reverse('password_reset'), {'email': '952775347@qq.com' })
        self.email = mail.outbox[0]

    def test_email_subject(self):
        self.assertEqual('[PornHub] Please reset your password', self.email.subject)

    def test_email_body(self):
        context = self.response.context
        token = context.get('token')
        uid = context.get('uid')
        password_reset_token_url = reverse('password_reset_confirm', kwargs={
            'uidb64': uid,
            'token': token
        })
        self.assertIn(password_reset_token_url, self.email.body)
        self.assertIn('testuser', self.email.body)
        self.assertIn('952775347@qq.com', self.email.body)

    def test_email_to(self):
        self.assertEqual(['952775347@qq.com', ], self.email.to)