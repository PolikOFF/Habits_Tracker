from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для пользователя."""
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    """Класс сериализатор для создания пользователя."""
    class Meta:
        """Класс отображения данных сериализатора."""
        model = User
        fields = ('email', 'password', 'telegram_id')

    def create(self, validated_data):
        """Метод создания пользователя с хешированием пароля."""
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
