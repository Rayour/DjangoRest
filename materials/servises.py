from django.utils import timezone

from materials.models import Lesson


def is_recent_course_update(course, lesson_id):
    """Метод проверки наличия недавних обновлений курса"""

    current_date_time = timezone.now()
    lessons = Lesson.objects.filter(course=course)
    is_recent_update = False

    for lesson_item in lessons:
        if lesson_item.id != lesson_id:
            if (current_date_time - lesson_item.updated_at).total_seconds() / 3600 < 4:
                is_recent_update = True
                break

    return is_recent_update


def get_email_list_from_subscription_list(subscriptions):
    """Получение списка email из подписок на обновление"""

    email_list = []
    for subscription_item in subscriptions:
        email_list.append(subscription_item.user.email)

    return email_list
