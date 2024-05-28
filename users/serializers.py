from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Класс сериализатор для пользователя."""
    class Meta:
        """Класс отображения данных сериализатора."""
        model = User
        fields = '__all__'

    def create(self, validated_data):
        """Метод создания пользователя с хешированием пароля."""
        password = make_password(validated_data['password'])
        validated_data['password'] = password
        user = User.objects.create_user(**validated_data)
        return user
