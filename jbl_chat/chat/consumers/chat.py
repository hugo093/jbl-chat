import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async, sync_to_async
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.other_user_username = self.scope["url_route"]["kwargs"]["username"]
        self.other_user = await database_sync_to_async(get_user_model().objects.get)(username=self.other_user_username)

        if not self.user.is_authenticated:
            await self.close()

        self.room_name = f"{min([self.user.username.lower(), self.other_user_username.lower()])}_{max([self.user.username.lower(), self.other_user_username.lower()])}"
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        from chat.models.messages import Message
        data = json.loads(text_data)
        message_text = data['content']

        receiver = await sync_to_async(get_user_model().objects.get)(username=self.other_user_username)
        message = await sync_to_async(Message.objects.create)(
            sender=self.user,
            receiver=receiver,
            content=message_text
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': message,
            }
        )

    async def chat_message(self, event):
        html = await sync_to_async(render_to_string)(
            'messages/partial.html',
            {'message': event['message'], "user": self.user}
        )
        await self.send(text_data=html)