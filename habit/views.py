from rest_framework import generics

from habit.models import Habit
from habit.pagination import HabitCustomPagination
from habit.seralizers import HabitSerializer


class HabitCreateAPIViewSet(generics.CreateAPIView):
    """Класс создания привычки."""
    serializer_class = HabitSerializer


class HabitListAPIViewSet(generics.ListAPIView):
    """Класс просмотра списка привычек."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitCustomPagination


class HabitRetrieveAPIViewSet(generics.RetrieveAPIView):
    """Класс просмотра одной привычки."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIViewSet(generics.UpdateAPIView):
    """Класс редактирования привычки."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIViewSet(generics.DestroyAPIView):
    """Класс удаления привычки."""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
