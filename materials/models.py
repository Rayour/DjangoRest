from django.db import models


class Course(models.Model):
    """Класс курса обучения"""

    name = models.CharField(max_length=300, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", help_text="Добавьте описание курса")
    image = models.ImageField(upload_to="media/", null=True, blank=True, verbose_name="Превью",
                              help_text="Загрузите изображение для превью курса")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        """Строковое представление объекта курса обучения"""

        return f"{self.name}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
        ordering = ["name", "created_at"]


class Lesson(models.Model):
    """Модель урока"""

    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", null=True, blank=True, help_text="Введите описание урока")
    image = models.ImageField(upload_to="media/", null=True, blank=True, verbose_name="Превью",
                              help_text="Загрузите изображение для превью урока")
    link = models.CharField(max_length=250, verbose_name="Ссылка на видео урока")
    course = models.ForeignKey(Course, verbose_name="Курс", on_delete=models.CASCADE, related_name="lessons")
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        """Строковое представление объекта урока"""

        return f"{self.name}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
        ordering = ["name", "created_at"]
