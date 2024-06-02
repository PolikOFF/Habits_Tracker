import datetime
from celery import shared_task

from habit.models import Habit
from habit.services import send_telegram_message


@shared_task
def habit_reminder():
    """Задача на отправку сообщения в телеграм, о времени выполнять привычку."""
    time_now = datetime.datetime.now().time()
    habits = Habit.objects.all()

    for habit in habits:
        if habit.time == time_now:
            message = f'Пора выполнить привычку!\n' \
                      f'Действие - {habit.action}\n' \
                      f'Место - {habit.place}\n'
            chat_id = habit.owner.telegram_id
            send_telegram_message(chat_id, message)
