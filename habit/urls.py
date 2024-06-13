from django.urls import path

from habit.apps import HabitConfig
from habit.views import (
    HabitCreateAPIViewSet,
    HabitListAPIViewSet,
    HabitRetrieveAPIViewSet,
    HabitUpdateAPIViewSet,
    HabitDestroyAPIViewSet
)

app_name = HabitConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIViewSet.as_view(), name='create-habit'),
    path('list/', HabitListAPIViewSet.as_view(), name='list-habit'),
    path('get/<int:pk>/', HabitRetrieveAPIViewSet.as_view(), name='get-habit'),
    path(
        'update/<int:pk>/',
        HabitUpdateAPIViewSet.as_view(),
        name='update-habit'),
    path(
        'delete/<int:pk>/',
        HabitDestroyAPIViewSet.as_view(),
        name='delete-habit'),
]
