from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    get_object_or_404,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course
from users.models import CustomUser, Payment, Subscription
from users.serializer import CustomUserSerializer, PaymentSerializer


class CustomUserCreateAPIView(CreateAPIView):
    """Класс для создания пользователя"""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Метод создания кастомного юзера с хешированием пароля"""

        user = serializer.save()
        user.set_password(user.password)
        user.save()


class CustomUserUpdateAPIView(UpdateAPIView):
    """Класс для обновления пользователя"""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDestroyAPIView(DestroyAPIView):
    """Класс для удаления пользователя"""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserRetrieveAPIView(RetrieveAPIView):
    """Класс для получения пользователя"""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserListAPIView(ListAPIView):
    """Класс для получения списка пользователей"""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class PaymentCreateAPIView(CreateAPIView):
    """Класс для создания платежа"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentUpdateAPIView(UpdateAPIView):
    """Класс для обновления платежа"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDestroyAPIView(DestroyAPIView):
    """Класс для удаления платежа"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveAPIView(RetrieveAPIView):
    """Класс для получения платежа"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentListAPIView(ListAPIView):
    """Класс для получения списка платежей"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["course", "lesson", "payment_method"]
    ordering_fields = [
        "payment_date",
    ]


class SubscriptionCreateOrDeleteAPIView(APIView):
    """Метод для добавления/удаления подписки пользователя на курс"""

    def post(self, request):
        user = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = user.subscriptions.filter(course__id=course_id)

        if subs_item.exists():
            subs_item.delete()
            message = "подписка удалена"
        else:
            subs_item = Subscription(user=user, course=course_item)
            subs_item.save()
            message = "подписка добавлена"

        return Response({"message": message})
