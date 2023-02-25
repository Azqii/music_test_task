from rest_framework import permissions


class IsAdminOrAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """
    Permission, позволяющий просмотр всем пользователям, создание только аутентифицированным,
    а удаление и редактирование только админу или автору.
    """

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and request.user.is_staff or
            request.user and request.user == obj.record_author
        )
