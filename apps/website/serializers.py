
from rest_framework import serializers

from apps.website.models import (
    Announcement,
    ContactMessage,
    FAQ,
    Newsletter,
)


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = (
            "id",
            "title",
            "content",
            "status",
            "published_at",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "published_at",
            "created_at",
            "updated_at",
        )


class AnnouncementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = (
            "title",
            "content",
            "status",
        )


class AnnouncementUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = (
            "title",
            "content",
            "status",
        )

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = (
            "id",
            "name",
            "email",
            "subject",
            "message",
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "status",
            "created_at",
            "updated_at",
        )


class ContactMessageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = (
            "status",
        )

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = (
            "id",
            "question",
            "answer",
            "is_active",
            "display_order",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class FAQCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = (
            "question",
            "answer",
            "is_active",
            "display_order",
        )


class FAQUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = (
            "question",
            "answer",
            "is_active",
            "display_order",
        )

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = (
            "id",
            "email",
            "is_active",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )


class NewsletterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = (
            "email",
        )