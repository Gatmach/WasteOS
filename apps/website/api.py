
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.common.api import BaseAdminModelViewSet

from apps.website.selectors import (
    list_announcements,
    get_published_announcements,
    
    list_contact_messages,

    list_faqs,
    get_active_faqs,

    list_newsletters,
    get_active_newsletters,
)

from apps.website.serializers import (
    AnnouncementSerializer,
    AnnouncementCreateSerializer,
    AnnouncementUpdateSerializer,

    ContactMessageSerializer,
    ContactMessageUpdateSerializer,

    FAQSerializer,
    FAQCreateSerializer,
    FAQUpdateSerializer,

    NewsletterSerializer,
    NewsletterCreateSerializer,
)

from apps.website.services import (
    create_announcement,
    update_announcement,
    publish_announcement,

    archive_announcement,
    create_contact_message,
    update_contact_message,
    mark_contact_message_in_progress,
    resolve_contact_message,

    create_faq,
    update_faq,
    activate_faq,
    deactivate_faq,

    create_newsletter,
    activate_newsletter,
    deactivate_newsletter,
)


# ============================================================================
# Announcement
# ============================================================================

class AnnouncementViewSet(BaseAdminModelViewSet):
    filterset_fields = (
        "status",
    )

    search_fields = (
        "title",
        "content",
    )

    ordering_fields = (
        "title",
        "created_at",
        "published_at",
    )

    ordering = (
        "-created_at",
    )

    def get_queryset(self):
        return list_announcements()

    def get_serializer_class(self):
        if self.action == "create":
            return AnnouncementCreateSerializer

        if self.action in (
            "update",
            "partial_update",
        ):
            return AnnouncementUpdateSerializer

        return AnnouncementSerializer

    def perform_create(self, serializer):
        serializer.instance = create_announcement(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = update_announcement(
            serializer.instance,
            **serializer.validated_data,
        )

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
    )
    def published(self, request):
        queryset = get_published_announcements()

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = AnnouncementSerializer(
                page,
                many=True,
            )
            return self.get_paginated_response(serializer.data)

        serializer = AnnouncementSerializer(
            queryset,
            many=True,
        )
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["post"],
    )
    def publish(self, request, pk=None):
        announcement = self.get_object()
        announcement = publish_announcement(announcement)

        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["post"],
    )
    def archive(self, request, pk=None):
        announcement = self.get_object()
        announcement = archive_announcement(announcement)

        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)


# ============================================================================
# Contact Message
# ============================================================================

class ContactMessageViewSet(BaseAdminModelViewSet):
    filterset_fields = (
        "status",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    ordering_fields = (
        "created_at",
        "updated_at",
        "name",
    )

    ordering = (
        "-created_at",
    )

    def get_queryset(self):
        return list_contact_messages()

    def get_serializer_class(self):
        if self.action == "create":
            return ContactMessageSerializer

        if self.action in (
            "update",
            "partial_update",
        ):
            return ContactMessageUpdateSerializer

        return ContactMessageSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.instance = create_contact_message(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = update_contact_message(
            serializer.instance,
            **serializer.validated_data,
        )

    @action(
        detail=True,
        methods=["post"],
    )
    def mark_in_progress(self, request, pk=None):
        contact_message = self.get_object()
        contact_message = mark_contact_message_in_progress(
            contact_message,
        )

        serializer = ContactMessageSerializer(contact_message)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["post"],
    )
    def resolve(self, request, pk=None):
        contact_message = self.get_object()
        contact_message = resolve_contact_message(
            contact_message,
        )

        serializer = ContactMessageSerializer(contact_message)
        return Response(serializer.data)

# ============================================================================
# FAQ
# ============================================================================

class FAQViewSet(BaseAdminModelViewSet):
    filterset_fields = (
        "is_active",
    )

    search_fields = (
        "question",
        "answer",
    )

    ordering_fields = (
        "display_order",
        "created_at",
        "question",
    )

    ordering = (
        "display_order",
    )

    def get_queryset(self):
        return list_faqs()

    def get_serializer_class(self):
        if self.action == "create":
            return FAQCreateSerializer

        if self.action in (
            "update",
            "partial_update",
        ):
            return FAQUpdateSerializer

        return FAQSerializer

    def perform_create(self, serializer):
        serializer.instance = create_faq(
            **serializer.validated_data,
        )

    def perform_update(self, serializer):
        serializer.instance = update_faq(
            serializer.instance,
            **serializer.validated_data,
        )

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
    )
    def active(self, request):
        queryset = get_active_faqs()

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = FAQSerializer(
                page,
                many=True,
            )
            return self.get_paginated_response(serializer.data)

        serializer = FAQSerializer(
            queryset,
            many=True,
        )
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["post"],
    )
    def activate(self, request, pk=None):
        faq = self.get_object()
        faq = activate_faq(faq)

        serializer = FAQSerializer(faq)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["post"],
    )
    def deactivate(self, request, pk=None):
        faq = self.get_object()
        faq = deactivate_faq(faq)

        serializer = FAQSerializer(faq)
        return Response(serializer.data)


# ============================================================================
# Newsletter
# ============================================================================

class NewsletterViewSet(BaseAdminModelViewSet):
    filterset_fields = (
        "is_active",
    )

    search_fields = (
        "email",
    )

    ordering_fields = (
        "email",
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    def get_queryset(self):
        return list_newsletters()

    def get_serializer_class(self):
        if self.action == "create":
            return NewsletterCreateSerializer

        return NewsletterSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.instance = create_newsletter(
            **serializer.validated_data,
        )

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
    )
    def active(self, request):
        queryset = get_active_newsletters()

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = NewsletterSerializer(
                page,
                many=True,
            )
            return self.get_paginated_response(serializer.data)

        serializer = NewsletterSerializer(
            queryset,
            many=True,
        )
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["post"],
    )
    def activate(self, request, pk=None):
        newsletter = self.get_object()
        newsletter = activate_newsletter(newsletter)

        serializer = NewsletterSerializer(newsletter)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["post"],
    )
    def deactivate(self, request, pk=None):
        newsletter = self.get_object()
        newsletter = deactivate_newsletter(newsletter)

        serializer = NewsletterSerializer(newsletter)
        return Response(serializer.data)