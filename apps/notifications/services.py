
from django.db import transaction

from apps.accounts.models import User

from apps.notifications.choices import NotificationChannel
from apps.notifications.models import (
    Notification,
    NotificationLog,
)


@transaction.atomic
def create_notification(
    *,
    user: User,
    title: str,
    message: str,
    notification_type: str,
    channel: str = NotificationChannel.IN_APP,
) -> Notification:
    return Notification.objects.create(
        user=user,
        title=title,
        message=message,
        notification_type=notification_type,
        channel=channel,
    )


@transaction.atomic
def mark_notification_as_read(
    *,
    notification: Notification,
) -> Notification:
    if not notification.is_read:
        notification.is_read = True
        notification.save(
            update_fields=[
                "is_read",
                "updated_at",
            ]
        )

    return notification


@transaction.atomic
def mark_all_notifications_as_read(
    *,
    user: User,
) -> int:
    return (
        Notification.objects
        .filter(
            user=user,
            is_read=False,
        )
        .update(is_read=True)
    )


@transaction.atomic
def delete_notification(
    *,
    notification: Notification,
) -> None:
    notification.delete()

@transaction.atomic
def create_notification_log(
    *,
    notification: Notification,
    response: str = "",
    is_successful: bool = True,
) -> NotificationLog:
    return NotificationLog.objects.create(
        notification=notification,
        response=response,
        is_successful=is_successful,
    )


@transaction.atomic
def send_notification(
    *,
    notification: Notification,
) -> NotificationLog:
    """
    Record an in-app notification delivery.

    External email/SMS providers will be integrated later.
    """

    if notification.channel == NotificationChannel.IN_APP:
        log = create_notification_log(
            notification=notification,
            response="Notification delivered in-app.",
            is_successful=True,
        )

        return log

    log = create_notification_log(
        notification=notification,
        response=(
            f"Delivery channel '{notification.channel}' "
            "is not configured."
        ),
        is_successful=False,
    )

    return log

