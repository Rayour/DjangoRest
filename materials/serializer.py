from rest_framework.serializers import ModelSerializer

from materials.models import Course


class CourseSerializer(ModelSerializer):
    """Сериализатор для класса курсов обучения"""

    class Meta:
        model = Course
        fields = '__all__'
