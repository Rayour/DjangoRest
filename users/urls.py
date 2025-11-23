from django.urls import path

from users.apps import UsersConfig
from users.views import (CustomUserCreateAPIView, CustomUserDestroyAPIView,
                         CustomUserListAPIView, CustomUserRetrieveAPIView,
                         CustomUserUpdateAPIView, PaymentListAPIView, PaymentCreateAPIView, PaymentUpdateAPIView,
                         PaymentRetrieveAPIView, PaymentDestroyAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path("", CustomUserListAPIView.as_view(), name="users_list"),
    path("create/", CustomUserCreateAPIView.as_view(), name="users_create"),
    path("<int:pk>/update/", CustomUserUpdateAPIView.as_view(), name="users_update"),
    path("<int:pk>/", CustomUserRetrieveAPIView.as_view(), name="users_retrieve"),
    path("<int:pk>/delete/", CustomUserDestroyAPIView.as_view(), name="users_delete"),
    path("payments/", PaymentListAPIView.as_view(), name="payment_list"),
    path("payments/create/", PaymentCreateAPIView.as_view(), name="payment_create"),
    path("payments/<int:pk>/update/", PaymentUpdateAPIView.as_view(), name="payment_update"),
    path("payments/<int:pk>/", PaymentRetrieveAPIView.as_view(), name="payment_retrieve"),
    path("payments/<int:pk>/delete/", PaymentDestroyAPIView.as_view(), name="payment_delete"),
]
