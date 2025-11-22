from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from users.models import CustomUser
from users.serializer import CustomUserSerializer


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
