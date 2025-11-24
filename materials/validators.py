import re

from django.core.exceptions import ValidationError


def lesson_link_validator(value):
    """Валидатор проверяет, что ссылка на урок ведет исключительно на youtube"""

    reg = re.compile("https:\/\/youtu.be\/[A-Za-z]+")
    if not bool(reg.match(value)):
        raise ValidationError("You can use youtube link only")
