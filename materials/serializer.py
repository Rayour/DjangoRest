from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Сериализатор для класса курсов обучения"""
    lessons_count = SerializerMethodField()

    def get_lessons_count(self, course):
        """Метод получения количества уроков курса"""
        return course.lessons.count()

    class Meta:
        model = Course
        fields = ('name', 'description', 'image', 'lessons_count', 'created_at', 'updated_at',)


class LessonSerializer(ModelSerializer):
    """Сериализатор для уроков курсов обучения"""

    class Meta:
        model = Lesson
        fields = '__all__'
