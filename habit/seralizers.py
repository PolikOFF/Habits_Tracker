from rest_framework import serializers

from habit.models import Habit
from habit.validators import (
    RewardValidator,
    TimeToCompleteValidator,
    PleasantHabitInRelatedHabitValidator,
    PleasantHabitNotHaveRelatedRewardValidator,
    PeriodicityHabitValidator
)


class HabitSerializer(serializers.ModelSerializer):
    """Класс сериализатора привычки."""
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardValidator('reward', 'related_habit'),
            TimeToCompleteValidator('time_to_complete'),
            PleasantHabitInRelatedHabitValidator('related_habit'),
            PleasantHabitNotHaveRelatedRewardValidator(
                'pleasant_habit', 'related_habit', 'reward'),
            PeriodicityHabitValidator('periodicity'),
        ]
