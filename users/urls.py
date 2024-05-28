from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIViewSet, UserListAPIViewSet, UserDetailAPIViewSet

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIViewSet.as_view(), name='user_create'),
    path('list/', UserListAPIViewSet.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailAPIViewSet.as_view(), name='user_detail'),
]
