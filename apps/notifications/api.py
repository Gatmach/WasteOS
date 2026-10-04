
from rest_framework import serializers
from apps.notifications.choices import (
    NotificationChannel,
    NotificationType,
)
from apps.notifications.models import (
    Notification,
    NotificationLog,
)

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            "id",
            "title",
            "message",
            "notification_type",
            "channel",
            "status",
            "is_read",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "status",
            "is_read",
            "created_at",
            "updated_at",
        )


class NotificationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationLog
        fields = (
            "id",
            "notification",
            "response",
            "is_successful",
            "sent_at",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "sent_at",
            "created_at",
            "updated_at",
        )


class CreateNotificationSerializer(serializers.Serializer):
    title = serializers.CharField(
        max_length=255,
    )

    message = serializers.CharField()

    notification_type = serializers.ChoiceField(
        choices=NotificationType.choices,
    )

    channel = serializers.ChoiceField(
        choices=NotificationChannel.choices,
        required=False,
        default=NotificationChannel.IN_APP,
    )