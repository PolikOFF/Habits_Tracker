from django.db import models
from users.models import NULLABLE


class Habit(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='создатель привычки', **NULLABLE),
    place = models.CharField(max_length=255, verbose_name='место выполнения привычки'),
    time = models.TimeField(default='14:00:00', verbose_name='время выполнения привычки'),
    action = models.CharField(max_length=255, verbose_name='действие'),
    pleasant_habit = models.BooleanField(verbose_name='признак приятной привычки'),
    related_habit = models.ForeignKey
