from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users.models import CustomUser, Payment, Subscription


class PaymentSerializer(ModelSerializer):
    """Сериализатор для платежа"""

    class Meta:
        model = Payment
        fields = "__all__"


class SubscriptionSerializer(ModelSerializer):
    """Сериализатор для подписки"""

    class Meta:
        model = Subscription
        fields = "__all__"


class CustomUserSerializer(ModelSerializer):
    """Сериализатор для пользователя"""

    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "payments",
            "phone_number",
            "city",
            "avatar",
            "username",
            "password",
            "subscriptions",
        )
