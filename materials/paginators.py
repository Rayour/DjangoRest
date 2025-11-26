from rest_framework.pagination import PageNumberPagination


class LessonsCoursesPaginator(PageNumberPagination):
    """Класс пагинатор для постраничного вывода уроков и курсов"""

    page_size = 10
    page_size_query_param = "per-page"
    max_page_size = 100
