from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIViewSet(generics.CreateAPIView):
    """Класс для создания User."""
    serializer_class = UserSerializer


class UserListAPIViewSet(generics.ListAPIView):
    """Класс для отображения списка User."""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailAPIViewSet(generics.RetrieveUpdateDestroyAPIView):
    """Класс для отображения, обновления и удаления User."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
