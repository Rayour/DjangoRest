from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """Класс доступов для модераторов"""

    message = "Creating and deleting not allowed"

    def has_permission(self, request, view):
        """Метод проверки наличия группы moders у пользователя"""

        return request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):
    """Класс доступов для владельцев"""

    def has_object_permission(self, request, view, obj):
        """Метод проверки принадлежности записи пользователю"""

        return (obj.owner == request.user) & ~request.user.groups.filter(
            name="moders"
        ).exists()
