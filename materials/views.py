from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from materials.models import Course, Lesson
from materials.paginators import LessonsCoursesPaginator
from materials.serializer import CourseSerializer, LessonSerializer
from users.permissions import IsModer, IsOwner


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(operation_description="Получение списка курсов"),
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(operation_description="Получение курса"),
)
@method_decorator(
    name="create", decorator=swagger_auto_schema(operation_description="Создание курса")
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(operation_description="Обновление курса"),
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(operation_description="Частичное обновление курса"),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(operation_description="Удаление курса"),
)
class CourseViewSet(ModelViewSet):
    """Вьюсет для курса обучения"""

    serializer_class = CourseSerializer
    pagination_class = LessonsCoursesPaginator

    def get_queryset(self):
        if self.request.user.groups.filter(name="moders").exists():
            return Course.objects.all()
        return Course.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """Метод создания с сохранением пользователя в качестве владельца"""
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        """Метод проверки прав"""

        if self.action == "create":
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsOwner | ~IsModer,)
        return super().get_permissions()


class LessonCreateAPIView(CreateAPIView):
    """Создание урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~IsModer)

    def perform_create(self, serializer):
        """Метод создания с сохранением пользователя в качестве владельца"""
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonRetrieveAPIView(RetrieveAPIView):
    """Получение урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsModer)


class LessonUpdateAPIView(UpdateAPIView):
    """Обновление урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsModer)


class LessonListAPIView(ListAPIView):
    """Получение списка уроков"""

    serializer_class = LessonSerializer
    pagination_class = LessonsCoursesPaginator

    def get_queryset(self):
        if self.request.user.groups.filter(name="moders").exists():
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonDestroyAPIView(DestroyAPIView):
    """Удаление урока"""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsOwner | ~IsModer)
