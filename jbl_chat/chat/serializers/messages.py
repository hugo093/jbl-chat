from django.contrib.auth import get_user_model
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers

from chat.models import Message


class MessageSerializer(serializers.ModelSerializer):
    receiver = serializers.SlugRelatedField(queryset=get_user_model().objects.all(), slug_field='username')
    sender = serializers.SlugRelatedField(read_only=True, slug_field='username')
    created = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Message
        fields = ['created', 'sender', 'receiver', 'content']

    def get_created(self, obj):
        return str(naturaltime(obj.created))