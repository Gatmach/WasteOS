from django.db.models import QuerySet

from apps.website.models import (
    Announcement,
    ContactMessage,
    FAQ,
    Newsletter,
)


# ============================================================================
# Announcement Selectors
# ============================================================================

def get_announcement(announcement_id) -> Announcement:
    return Announcement.objects.get(pk=announcement_id)


def list_announcements() -> QuerySet[Announcement]:
    return Announcement.objects.all()


def get_published_announcements() -> QuerySet[Announcement]:
    return Announcement.objects.filter(
        status="published",
    )


# ============================================================================
# Contact Message Selectors
# ============================================================================

def get_contact_message(contact_message_id) -> ContactMessage:
    return ContactMessage.objects.get(pk=contact_message_id)


def list_contact_messages() -> QuerySet[ContactMessage]:
    return ContactMessage.objects.all()


def get_contact_messages_by_status(
    status,
) -> QuerySet[ContactMessage]:
    return ContactMessage.objects.filter(
        status=status,
    )


# ============================================================================
# FAQ Selectors
# ============================================================================

def get_faq(faq_id) -> FAQ:
    return FAQ.objects.get(pk=faq_id)


def list_faqs() -> QuerySet[FAQ]:
    return FAQ.objects.all()


def get_active_faqs() -> QuerySet[FAQ]:
    return FAQ.objects.filter(
        is_active=True,
    )


# ============================================================================
# Newsletter Selectors
# ============================================================================

def get_newsletter(newsletter_id) -> Newsletter:
    return Newsletter.objects.get(pk=newsletter_id)

def list_newsletters() -> QuerySet[Newsletter]:
    return Newsletter.objects.all().order_by("-created_at")


def get_active_newsletters() -> QuerySet[Newsletter]:
    return Newsletter.objects.filter(
        is_active=True,
    ).order_by("-created_at")