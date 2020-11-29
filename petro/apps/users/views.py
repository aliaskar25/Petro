from rest_framework.generics import ListAPIView

from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import UserSerializer



User = get_user_model()


class UserListAPIView(ListAPIView):
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['registration_date', ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
