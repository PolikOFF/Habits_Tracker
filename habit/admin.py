from django.contrib import admin


@admin.register
class HabitAdmin(admin.ModelAdmin):
    """Класс для регистрации модели привычки в административной панели."""
    list_display = ('user', 'action')
