from django.contrib.auth import get_user_model
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from chat.serializers.users import UserListSerializer


class UserViewSet(GenericViewSet):
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name', 'username']


    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def get_template_names(self):
        if self.action == 'list':
            return ["users/list.html"]
        raise NotImplementedError

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        raise NotImplementedError

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"object_list": serializer.data})


