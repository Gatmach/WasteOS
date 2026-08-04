from django.contrib import admin

from .models import (
    Announcement,
    ContactMessage,
    FAQ,
    Newsletter,
)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )

    list_filter = (
        "status",
    )

    ordering = (
        "-created_at",
    )


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "published_at",
    )

    list_filter = (
        "status",
    )

    ordering = (
        "-created_at",
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "display_order",
    )


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "is_active",
        "created_at",
    )

    search_fields = (
        "email",
    )

    list_filter = (
        "is_active",
    )