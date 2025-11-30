from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (CustomUserCreateAPIView, CustomUserDestroyAPIView,
                         CustomUserListAPIView, CustomUserRetrieveAPIView,
                         CustomUserUpdateAPIView, PaymentCreateAPIView,
                         PaymentDestroyAPIView, PaymentListAPIView,
                         PaymentRetrieveAPIView, PaymentStatusCheckAPIView,
                         PaymentUpdateAPIView,
                         SubscriptionCreateOrDeleteAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path("", CustomUserListAPIView.as_view(), name="users_list"),
    path("create/", CustomUserCreateAPIView.as_view(), name="users_create"),
    path("<int:pk>/update/", CustomUserUpdateAPIView.as_view(), name="users_update"),
    path("<int:pk>/", CustomUserRetrieveAPIView.as_view(), name="users_retrieve"),
    path("<int:pk>/delete/", CustomUserDestroyAPIView.as_view(), name="users_delete"),
    path("payments/", PaymentListAPIView.as_view(), name="payment_list"),
    path("payments/create/", PaymentCreateAPIView.as_view(), name="payment_create"),
    path(
        "payments/<int:pk>/update/",
        PaymentUpdateAPIView.as_view(),
        name="payment_update",
    ),
    path(
        "payments/<int:pk>/status/",
        PaymentStatusCheckAPIView.as_view(),
        name="payment_status_check",
    ),
    path(
        "payments/<int:pk>/", PaymentRetrieveAPIView.as_view(), name="payment_retrieve"
    ),
    path(
        "payments/<int:pk>/delete/",
        PaymentDestroyAPIView.as_view(),
        name="payment_delete",
    ),
    path(
        "subscription/",
        SubscriptionCreateOrDeleteAPIView.as_view(),
        name="subscription",
    ),
    path(
        "token/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
]
