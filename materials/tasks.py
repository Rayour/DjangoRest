from celery import shared_task
from django.core.mail import send_mail

from config.settings import DEFAULT_FROM_EMAIL


@shared_task
def send_course_update_email(email_list, course_name):
    """Отправка письма об обновлении курса"""
    print(email_list)
    from_email = DEFAULT_FROM_EMAIL
    message = f'''Обновилась информация по курсу "{course_name}"'''
    send_mail("Обновление курса", message, from_email, email_list)
