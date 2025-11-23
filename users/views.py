from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from users.models import CustomUser, Payment
from users.serializer import CustomUserSerializer, PaymentSerializer


class CustomUserCreateAPIView(CreateAPIView):
    """Класс для создания пользователя"""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


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
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_date', ]
