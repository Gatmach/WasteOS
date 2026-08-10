
from django.db.models import QuerySet

from apps.accounts.models import User

from apps.notifications.models import (
    Notification,
    NotificationLog,
)


def get_user_notifications(
    user: User,
) -> QuerySet[Notification]:
    return (
        Notification.objects
        .filter(user=user)
        .select_related("user")
        .order_by("-created_at")
    )


def get_unread_notifications(
    user: User,
) -> QuerySet[Notification]:
    return (
        Notification.objects
        .filter(
            user=user,
            is_read=False,
        )
        .select_related("user")
        .order_by("-created_at")
    )


def get_notification(
    notification_id,
    user: User,
) -> Notification | None:
    return (
        Notification.objects
        .filter(
            id=notification_id,
            user=user,
        )
        .select_related("user")
        .first()
    )


def get_unread_notification_count(
    user: User,
) -> int:
    return Notification.objects.filter(
        user=user,
        is_read=False,
    ).count()


def get_notification_logs(
    notification: Notification,
) -> QuerySet[NotificationLog]:
    return (
        NotificationLog.objects
        .filter(notification=notification)
        .order_by("-sent_at")
    )