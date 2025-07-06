from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from chat.models import Message


class TestMessagesAPI(APITestCase):
    def setUp(self):
        # create two users
        self.user = get_user_model().objects.create_user(username='test', password='random')
        self.other_user = get_user_model().objects.create_user(username='test_other', password='random_other')
        self.another_user = get_user_model().objects.create_user(username='test_another_user', password='random_other')


    def test_list_messages(self):
        res = self.client.get(reverse('messages-list-by-receiver', kwargs={'other_username': self.user.username}))
        self.assertEqual(res.status_code, 403)

        self.assertTrue(self.client.login(username='test', password='random'))

        # create messages
        Message.objects.create(sender=self.user, receiver=self.other_user, content='hello')
        Message.objects.create(sender=self.user, receiver=self.another_user, content='there')
        Message.objects.create(sender=self.other_user, receiver=self.another_user, content='kenobi')

        res = self.client.get(reverse('messages-list-by-receiver', kwargs={'other_username': self.other_user.username}))

        self.assertIn('hello', res.content.decode())
        self.assertNotIn('there', res.content.decode())
        self.assertNotIn('kenobi', res.content.decode())

        res = self.client.get(reverse('messages-list-by-receiver', kwargs={'other_username': self.another_user.username}))

        self.assertNotIn('hello', res.content.decode())
        self.assertIn('there', res.content.decode())
        self.assertNotIn('kenobi', res.content.decode())

        self.client.logout()

        self.assertTrue(self.client.login(username='test_other', password='random_other'))

        res = self.client.get(reverse('messages-list-by-receiver', kwargs={'other_username': self.user.username}))

        self.assertIn('hello', res.content.decode())
        self.assertNotIn('there', res.content.decode())
        self.assertNotIn('kenobi', res.content.decode())

        res = self.client.get(
            reverse('messages-list-by-receiver', kwargs={'other_username': self.another_user.username}))

        self.assertNotIn('hello', res.content.decode())
        self.assertNotIn('there', res.content.decode())
        self.assertIn('kenobi', res.content.decode())

