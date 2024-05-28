from rest_framework.serializers import ValidationError


class RewardValidator:
    """Класс валидации вознаграждения."""

    def __init__(self, reward, related_habit):
        self.reward = reward
        self.related_habit = related_habit

    def __call__(self, value):
        if value.get(self.reward) and value.get(self.related_habit):
            raise ValidationError(
                "Не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки. Можно заполнить только одно из двух полей.")


class TimeToCompleteValidator:
    """Класс валидации выполнения привычки не более 120 секунд."""
    def __init__(self, time_to_complete):
        self.time_to_complete = time_to_complete

    def __call__(self, value):
        if self.time_to_complete in value:
            time_duration = value[self.time_to_complete]
            if time_duration > 120:
                raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


class PleasantHabitInRelatedHabitValidator:
    """Класс валидации того, что в связанные привычки могут попадать только привычки с признаком приятной привычки."""
    def __init__(self, related_habit, pleasant_habit):
        self.related_habit = related_habit
        self.pleasant_habit = pleasant_habit

    def __call__(self, value):
        if value:
            related_habit = value[self.related_habit]
            pleasant_habit = value[self.pleasant_habit]
            if related_habit and not pleasant_habit:
                raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')


class PleasantHabitNotHaveRelatedRewardValidator:
    """Класс валидации того, что у приятной привычки не может быть награды или связанной привычки."""
    def __init__(self, pleasant_habit, related_habit, reward):
        self.pleasant_habit = pleasant_habit
        self.related_habit = related_habit
        self.reward = reward

    def __call__(self, value):
        if value:
            pleasant_habit = value[self.pleasant_habit]
            related_habit = value[self.related_habit]
            reward = value[self.reward]
            if pleasant_habit and (related_habit or reward):
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')


class PeriodicityHabitValidator:
    pass
