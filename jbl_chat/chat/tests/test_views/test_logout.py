from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class TestLogout(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='random')


    def test_login(self):
        res = self.client.post(reverse('logout'))
        self.assertRedirects(res, reverse('login') + f"?next={reverse('logout')}")

        self.client.login(username='test', password='random')
        res = self.client.post(reverse('logout'))
        self.assertRedirects(res, reverse('login'))
        self.assertFalse(res.wsgi_request.user.is_authenticated)