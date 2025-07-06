from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class TestLogin(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='random')


    def test_login(self):
        res = self.client.get(reverse('home'))
        self.assertRedirects(res, reverse('login') +"?next=/")

        res = self.client.post(reverse('login'), data={'username': 'wrong', 'password': 'wrong'})
        self.assertEqual(res.status_code, 200)
        self.assertFormError(res.context_data['form'], None, ['Please enter a correct username and password. Note that both fields may be case-sensitive.'])

        res = self.client.post(reverse('login'), data={'username': 'test', 'password': 'random'})
        self.assertRedirects(res, reverse('home'))
        self.assertTrue(res.wsgi_request.user.is_authenticated)


