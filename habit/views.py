from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from habit.models import Habit
from habit.pagination import HabitCustomPagination
from habit.permissions import IsOwner
from habit.seralizers import HabitSerializer


class HabitCreateAPIViewSet(generics.CreateAPIView):
    """Класс создания привычки."""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Метод для привязки привычки к пользователю."""
        serializer.save(user=self.request.user)


class HabitListAPIViewSet(generics.ListAPIView):
    """Класс просмотра списка привычек пользователя."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitCustomPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Переопределение метода, для отображения привычек, которые принадлежат автору."""
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListAPIViewSet(generics.ListAPIView):
    """Класс просмотра списка публичных привычек."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitCustomPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Переопределение метода, для отображения только публичных привычек."""
        return Habit.objects.filter(is_public=True)


class HabitRetrieveAPIViewSet(generics.RetrieveAPIView):
    """Класс просмотра одной привычки."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIViewSet(generics.UpdateAPIView):
    """Класс редактирования привычки."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIViewSet(generics.DestroyAPIView):
    """Класс удаления привычки."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner, IsAdminUser]
