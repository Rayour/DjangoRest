from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    """Сериализатор для уроков курсов обучения"""

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    """Сериализатор для класса курсов обучения"""
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, course):
        """Метод получения количества уроков курса"""
        return course.lessons.count()

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'image', 'lessons_count', 'lessons', 'created_at', 'updated_at',)
