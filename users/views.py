from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course
from users.models import CustomUser, Payment, Subscription
from users.serializer import CustomUserSerializer, PaymentSerializer
from users.servises import (create_stripe_price, create_stripe_product,
                            create_stripe_session, get_stripe_payment_status)


class CustomUserCreateAPIView(CreateAPIView):
    """Создание пользователя"""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Метод создания кастомного юзера с хешированием пароля"""

        user = serializer.save()
        user.set_password(user.password)
        user.save()


class CustomUserUpdateAPIView(UpdateAPIView):
    """Обновление пользователя"""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDestroyAPIView(DestroyAPIView):
    """Удаление пользователя"""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserRetrieveAPIView(RetrieveAPIView):
    """Получение пользователя"""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserListAPIView(ListAPIView):
    """Получение списка пользователей"""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class PaymentCreateAPIView(CreateAPIView):
    """Создание платежа"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        """Метод создания платежа"""

        payment = serializer.save()
        if payment.course:
            payment_product = payment.course.name
        else:
            payment_product = payment.lesson.name
        stripe_product_id = create_stripe_product(payment_product)
        stripe_price_id = create_stripe_price(payment.payment_amount, stripe_product_id)
        payment.session_id, payment.payment_url = create_stripe_session(stripe_price_id)
        payment.save()


class PaymentUpdateAPIView(UpdateAPIView):
    """Обновление платежа"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDestroyAPIView(DestroyAPIView):
    """Удаление платежа"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveAPIView(RetrieveAPIView):
    """Получение платежа"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentStatusCheckAPIView(APIView):
    """Получение статуса платежа"""

    custom_success_response = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "message": openapi.Schema(
                type=openapi.TYPE_STRING, description="payment_status"
            )
        },
    )

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: custom_success_response},
    )
    def get(self, request, *args, **kwargs):
        payment_id = self.kwargs.get("pk")
        payment_item = get_object_or_404(Payment, pk=payment_id)

        if payment_item:
            payment_status = get_stripe_payment_status(payment_item.session_id)
            payment_item.payment_status = payment_status
            payment_item.save()
            message = {"payment_status": payment_status}
        else:
            message = {"error": f"no payment with id={payment_id}"}

        return Response(message)


class PaymentListAPIView(ListAPIView):
    """Получение списка платежей"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["course", "lesson", "payment_method"]
    ordering_fields = [
        "payment_date",
    ]


class SubscriptionCreateOrDeleteAPIView(APIView):
    """Добавление/удаление подписки пользователя на обновления курса.
    Если пользователь уже подписан на курс - подписка будет удалена, иначе - добавлена.
    """

    request_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "course": openapi.Schema(
                type=openapi.TYPE_INTEGER, description="идентификатор курса"
            )
        },
        required=["course"],
    )

    custom_success_response = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "message": openapi.Schema(
                type=openapi.TYPE_STRING, description="подписка добавлена"
            )
        },
    )

    @swagger_auto_schema(
        request_body=request_schema,
        responses={status.HTTP_200_OK: custom_success_response},
    )
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
