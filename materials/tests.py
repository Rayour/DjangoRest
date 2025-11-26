from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import CustomUser


class LessonsTestCase(APITestCase):
    """Класс для тестирования CRUD уроков"""

    def setUp(self):
        """Метод создания тестовых данных"""

        self.user = CustomUser.objects.create(email="test@test.ru", username="test")
        self.course = Course.objects.create(
            name="course1", description="description1", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name="lesson1",
            course=self.course,
            owner=self.user,
            link="https://youtu.be/asdfgh",
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """Метод для проверки просмотра урока"""
        url = reverse("materials:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        """Метод для проверки создания урока"""

        url = reverse("materials:lessons_create")
        data = {
            "name": "lesson2",
            "link": "https://youtu.be/qwerty",
            "course": self.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        """Метод для проверки обновления урока"""

        url = reverse("materials:lessons_update", args=(self.lesson.pk,))
        data = {
            "name": "lesson11",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "lesson11")

    def test_lesson_delete(self):
        """Метод для проверки удаления урока"""

        url = reverse("materials:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        """Метод для проверки списка уроков"""

        url = reverse("materials:lessons_list")
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["count"], 1)
        self.assertEqual(data["next"], None)
        self.assertEqual(data["previous"], None)
        self.assertEqual(data["results"][0]["id"], self.lesson.pk)
        self.assertEqual(data["results"][0]["name"], self.lesson.name)
        self.assertEqual(data["results"][0]["link"], self.lesson.link)
        self.assertEqual(data["results"][0]["course"], self.course.pk)
        self.assertEqual(data["results"][0]["owner"], self.user.pk)
