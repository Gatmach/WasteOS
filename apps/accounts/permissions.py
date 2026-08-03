
from rest_framework.permissions import BasePermission


class IsSuperAdmin(BasePermission):
    """
    Placeholder permission.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated