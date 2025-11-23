from rest_framework.serializers import ModelSerializer

from users.models import CustomUser, Payment


class CustomUserSerializer(ModelSerializer):
    """Сериализатор для пользователя"""

    class Meta:
        model = CustomUser
        fields = '__all__'


class PaymentSerializer(ModelSerializer):
    """Сериализатор для платежа"""

    class Meta:
        model = Payment
        fields = '__all__'
