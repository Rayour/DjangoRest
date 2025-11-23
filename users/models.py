from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Модель кастомного пользователя"""

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name="Телефон",
                                    help_text="Необязательное поле. Введите Ваш номер телефона")
    city = models.CharField(max_length=30, null=True, blank=True, verbose_name="Город",
                            help_text="Необязательное поле. Укажите Ваш город")
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True, verbose_name="Аватар",
                               help_text="Необязательное поле. Загрузите изображение для Вашего профиля")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        """Строковое представление пользователя"""

        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
