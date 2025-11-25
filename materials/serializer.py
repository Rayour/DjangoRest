from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson
from materials.validators import lesson_link_validator
from users.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для уроков курсов обучения"""

    link = serializers.CharField(validators=[lesson_link_validator])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для класса курсов обучения"""

    lessons_count = SerializerMethodField()
    is_subscribed = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, course):
        """Метод получения количества уроков курса"""
        return course.lessons.count()

    def get_is_subscribed(self, course):
        """Метод получения признака подписки пользователя на курс"""

        user = self.context["request"].user
        return bool(Subscription.objects.filter(user=user, course=course).exists())

    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "description",
            "image",
            "lessons_count",
            "lessons",
            "is_subscribed",
            "created_at",
            "updated_at",
        )
