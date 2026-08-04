from django.db.models import Q, QuerySet

from apps.accounts.models import User


def get_user(user_id: int) -> User:
    return User.objects.get(pk=user_id)


def list_users() -> QuerySet:
    return User.objects.all()


def get_active_users() -> QuerySet:
    return User.objects.filter(is_active=True)


def get_users_by_role(role: str) -> QuerySet:
    return User.objects.filter(role=role)


def search_users(query: str) -> QuerySet:
    return User.objects.filter(
        Q(username__icontains=query)
        | Q(first_name__icontains=query)
        | Q(last_name__icontains=query)
        | Q(email__icontains=query)
    )