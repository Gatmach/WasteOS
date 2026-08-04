from rest_framework.permissions import BasePermission

from apps.accounts.choices import UserRole


class HasRole(BasePermission):
    """
    Base permission class for role-based access control.

    Django superusers automatically bypass role checks.
    """

    allowed_roles = ()

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        return user.role in self.allowed_roles


class IsSuperAdmin(HasRole):
    allowed_roles = (
        UserRole.SUPER_ADMIN,
    )


class IsOrganizationAdmin(HasRole):
    allowed_roles = (
        UserRole.ORGANIZATION_ADMIN,
    )


class IsFacilityManager(HasRole):
    allowed_roles = (
        UserRole.FACILITY_MANAGER,
    )


class IsSupervisor(HasRole):
    allowed_roles = (
        UserRole.SUPERVISOR,
    )


class IsDriver(HasRole):
    allowed_roles = (
        UserRole.DRIVER,
    )


class IsTechnician(HasRole):
    allowed_roles = (
        UserRole.TECHNICIAN,
    )