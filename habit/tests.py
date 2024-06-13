from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@test.ru',
            password='test',
            is_superuser=True,
            is_staff=True,
        )
        # аутентификация клиента
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            action='действие',
            place='место',
            periodicity='1',
            time_to_complete='100'
        )

    def test_get_list(self):
        """Тест просмотра списка привычек."""

        response = self.client.get("/habit/list/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        """Тест на создание привычки."""
        data = {
            'action': 'действие',
            'place': 'место',
            'periodicity': '1',
            'time_to_complete': '100'
        }

        response = self.client.post('/habit/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        """Тест на обновление привычки."""
        habit = Habit.objects.create(
            place="test",
            action="test",
            periodicity=1,
            time_to_complete=100,
            owner=self.user
        )

        data = {'place': 'test1'}

        response = self.client.patch(f'/habit/update/{habit.id}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        """Тест на удаление привычки."""
        habit = Habit.objects.create(
            place="test",
            action="test",
            periodicity=1,
            time_to_complete=100,
            owner=self.user
        )

        response = self.client.delete(f'/habit/delete/{habit.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(Habit.objects.filter(pk=habit.pk).exists())

    def test_retrieve(self):
        """Тест просмотра одной привычки."""
        habit = Habit.objects.create(
            place="test",
            action="test",
            periodicity=1,
            time_to_complete=100,
            owner=self.user
        )

        response = self.client.get(f'/habit/get/{habit.id}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_time_to_complete_habit(self):
        """Тест валидации привычки более 120 секунд."""
        data = {
            'action': 'действие',
            'place': 'место',
            'periodicity': '1',
            'time_to_complete': '121'
        }

        response = self.client.post('/habit/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_periodicity_habit(self):
        """Тест на проверку валидации периодичности привычки от 1 до 7."""
        data = {
            'action': 'действие',
            'place': 'место',
            'periodicity': '9',
            'time_to_complete': '100'
        }

        response = self.client.post('/habit/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
