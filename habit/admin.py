from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Класс для регистрации модели привычки в административной панели."""
    list_display = ('owner', 'action', 'time',)
