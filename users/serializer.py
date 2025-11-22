from rest_framework.serializers import ModelSerializer

from users.models import CustomUser


class CustomUserSerializer(ModelSerializer):
    """Сериализатор для пользователя"""

    class Meta:
        model = CustomUser
        fields = '__all__'
