from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.utils import timezone

from users.models import CustomUser


@shared_task
def block_unactive_users():
    """Блокирует неактивных пользователей"""

    current_date_time = timezone.now()
    date_time_to_block = current_date_time + relativedelta(months=-1)
    unactive_users = CustomUser.objects.filter(last_login__lt=date_time_to_block)
    unactive_users.update(is_active=False)
