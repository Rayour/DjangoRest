from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Модель кастомного пользователя"""

    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name="Телефон",
        help_text="Необязательное поле. Введите Ваш номер телефона",
    )
    city = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name="Город",
        help_text="Необязательное поле. Укажите Ваш город",
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        null=True,
        blank=True,
        verbose_name="Аватар",
        help_text="Необязательное поле. Загрузите изображение для Вашего профиля",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        """Строковое представление пользователя"""

        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Payment(models.Model):
    """Модель платежа"""

    from materials.models import Course, Lesson

    PAYMENT_METHODS = [("cash", "наличные"), ("transfer", "перевод на счет")]

    user = models.ForeignKey(
        CustomUser,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="payments",
    )
    course = models.ForeignKey(
        Course,
        verbose_name="Курс",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="payments",
    )
    lesson = models.ForeignKey(
        Lesson,
        verbose_name="Урок",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="payments",
    )
    payment_date = models.DateTimeField(
        verbose_name="Дата оплаты", blank=True, null=True
    )
    payment_amount = models.FloatField(verbose_name="Сумма платежа")
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        """Строковое представление объекта платежа"""

        return f"{self.payment_date}"

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
        ordering = ["payment_date", "created_at"]
