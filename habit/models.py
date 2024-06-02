from django.db import models
from users.models import NULLABLE


class Habit(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='создатель привычки', **NULLABLE)
    place = models.CharField(max_length=255, verbose_name='место выполнения привычки', **NULLABLE)
    time = models.TimeField(default='14:00:00', verbose_name='время выполнения привычки', **NULLABLE)
    action = models.CharField(default='создать действие', max_length=255, verbose_name='действие')
    pleasant_habit = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.IntegerField(verbose_name='периодичность выполнения(в днях)')
    reward = models.CharField(max_length=150, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.IntegerField(verbose_name='время на выполнение(в секундах)')
    is_public = models.BooleanField(default=False, verbose_name='признак публикации')

    def __str__(self):
        return f'Complete - {self.action} in {self.time_to_complete}.'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('id',)
