from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from users.apps import UsersConfig
from users.views import (
    UserCreateAPIViewSet,
    UserListAPIViewSet,
    UserDetailAPIViewSet)

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIViewSet.as_view(), name='user_create'),
    path('list/', UserListAPIViewSet.as_view(), name='user_list'),
    path('user/<int:pk>/', UserDetailAPIViewSet.as_view(), name='user_detail'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
