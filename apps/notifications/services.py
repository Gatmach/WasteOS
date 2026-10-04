
from django.db import transaction

from apps.accounts.models import User
from apps.notifications.choices import (
    NotificationChannel,
    NotificationStatus,
    NotificationType,
)

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
    notification_type: NotificationType | str,
    channel: NotificationChannel | str = NotificationChannel.IN_APP,
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
    notifications = Notification.objects.filter(
        user=user,
        is_read=False,
    )

    updated_count = 0

    for notification in notifications:
        notification.is_read = True
        notification.save(
            update_fields=[
                "is_read",
                "updated_at",
            ]
        )
        updated_count += 1

    return updated_count


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
    Record notification delivery and update its delivery status.

    External email/SMS providers will be integrated later.
    """

    if notification.channel == NotificationChannel.IN_APP:
        log = create_notification_log(
            notification=notification,
            response="Notification delivered in-app.",
            is_successful=True,
        )

        mark_notification_as_sent(
            notification=notification,
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

    mark_notification_as_failed(
        notification=notification,
    )

    return log

@transaction.atomic
def mark_notification_as_sent(
    *,
    notification: Notification,
) -> Notification:
    notification.status = NotificationStatus.SENT

    notification.save(
        update_fields=[
            "status",
            "updated_at",
        ]
    )

    return notification


@transaction.atomic
def mark_notification_as_failed(
    *,
    notification: Notification,
) -> Notification:
    notification.status = NotificationStatus.FAILED

    notification.save(
        update_fields=[
            "status",
            "updated_at",
        ]
    )

    return notification

