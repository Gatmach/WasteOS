from django.contrib import admin

from .models import Notification, NotificationLog


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "notification_type",
        "status",
        "created_at",
    )

    search_fields = (
        "title",
        "user__username",
    )

    list_filter = (
        "notification_type",
        "status",
    )

    autocomplete_fields = (
        "user",
    )

    list_select_related = (
        "user",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 25


@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):
    list_display = (
        "notification",
        "sent_at",
        "response",
        "is_successful",
    )

    autocomplete_fields = (
        "notification",
    )

    ordering = (
        "-sent_at",
    )

    readonly_fields = (
        "sent_at",
    )

    list_per_page = 25