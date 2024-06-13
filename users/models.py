from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        max_length=100,
        verbose_name='электронная почта')
    telegram_id = models.CharField(
        max_length=100,
        verbose_name='id телеграм-чата',
        **NULLABLE)
    name = models.CharField(
        max_length=200,
        verbose_name='имя пользователя',
        **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.name:
            return f'Имя - {self.name}, Электронная почта - {self.email}.'
        return f'Электронная почта - {self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
