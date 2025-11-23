from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """Класс доступов для модераторов"""

    message = "Creating and deleting not allowed"

    def has_permission(self, request, view):
        """Метод проверки наличия группы moders у пользователя"""

        return request.user.groups.filter(name="moders").exists()
