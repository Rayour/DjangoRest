from django.urls import path

from users.apps import UsersConfig
from users.views import (CustomUserCreateAPIView, CustomUserDestroyAPIView,
                         CustomUserListAPIView, CustomUserRetrieveAPIView,
                         CustomUserUpdateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path("", CustomUserListAPIView.as_view(), name="users_list"),
    path("create/", CustomUserCreateAPIView.as_view(), name="users_create"),
    path("<int:pk>/update/", CustomUserUpdateAPIView.as_view(), name="users_update"),
    path("<int:pk>/", CustomUserRetrieveAPIView.as_view(), name="users_retrieve"),
    path("<int:pk>/delete/", CustomUserDestroyAPIView.as_view(), name="users_delete"),
]
