from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='test@test.com',
            password='test',
            telegram_id='123123123123',
            name='test'
        )

        self.client.force_authenticate(user=self.user)

    def test_create(self):
        """Тест на создание пользователя."""
        data = {
            'email': 'test@example.com',
            'password': '123qwe123qwe',
            'telegram_id': '123123123123',
            'name': 'test'
        }

        response = self.client.post('/users/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        """Тест на изменение данных пользователя."""
        self.user = User.objects.create(
            email='test@example.com',
            password='test',
            telegram_id='123123123123',
            name='test'
        )

        data = {'telegram_id': '321321321321'}

        response = self.client.patch(f'/users/user/{self.user.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        """Тест на удаление пользователя."""
        self.user = User.objects.create(
            email='test@example.com',
            password='test',
            telegram_id='123123123123',
            name='test'
        )

        response = self.client.delete(f'/users/user/{self.user.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())

    def test_list(self):
        """Тест просмотра списка пользователей."""
        response = self.client.get("/users/list/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
