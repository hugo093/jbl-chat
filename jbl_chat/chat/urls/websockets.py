from django.urls import path

from chat.consumers.chat import ChatConsumer

websocket_urlpatterns = [
        path("ws/chat/<str:username>/", ChatConsumer.as_asgi())
]