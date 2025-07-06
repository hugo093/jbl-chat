from django.conf import settings
from django.urls import path, include
from rest_framework import routers

from chat.viewsets.messages import MessageViewSet
from chat.viewsets.users import UserViewSet

router = routers.DefaultRouter() if settings.DEBUG else routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('', include(router.urls))
]