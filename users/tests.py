from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course
from users.models import CustomUser, Subscription


class SubscriptionTestCase(APITestCase):
    """Класс для тестирования подписки на курс"""

    def setUp(self):
        """Метод создания тестовых данных"""

        self.user = CustomUser.objects.create(email="test@test.ru", username="test")
        self.course = Course.objects.create(
            name="course1", description="description1", owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_subscription_create_delete(self):
        """Метод для проверки подписки и отписки"""
        url = reverse("users:subscription")
        data = {"course": self.course.pk}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.all().count(), 1)
        self.assertEqual(response.json()["message"], "подписка добавлена")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.all().count(), 0)
        self.assertEqual(response.json()["message"], "подписка удалена")
