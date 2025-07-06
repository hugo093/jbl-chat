from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from chat.forms.messages import MessageCreateForm
from chat.models import Message
from chat.serializers.messages import MessageSerializer


class MessageViewSet(GenericViewSet):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Message.objects.all().select_related('sender', 'receiver')
    renderer_classes = [TemplateHTMLRenderer]

    def get_template_names(self):
        if self.action == 'list_by_other_user':
            return ["messages/list.html"]
        raise NotImplementedError
    
    @action(detail=False, url_path='(?P<other_username>[^/.]+)/list', methods=['GET'], url_name='list-by-receiver')
    def list_by_other_user(self, request, other_username, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(sender__username__in=[self.request.user.username, other_username],  receiver__username__in=[self.request.user.username, other_username]))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        try:
            other_person = get_user_model().objects.get(username=other_username)
        except get_user_model().DoesNotExist:
            other_person = None

        if other_person:
            other_person_label = f"{other_person.first_name} {other_person.last_name}" if other_person.first_name or other_person.last_name else f"{other_person.username}"
        else:
            other_person_label = "Unknown user"

        return Response({"object_list": serializer.data, "other_username": other_username, "other_person_label": other_person_label, "form_message": MessageCreateForm(initial={'receiver': other_username})})
