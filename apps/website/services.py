from django.db import transaction

from apps.website.choices import (
    AnnouncementStatus,
    MessageStatus,
)
from apps.website.models import (
    Announcement,
    ContactMessage,
    FAQ,
    Newsletter,
)


# ============================================================================
# Announcement Services
# ============================================================================

@transaction.atomic
def create_announcement(
    *,
    title,
    content,
    status=AnnouncementStatus.DRAFT,
) -> Announcement:
    return Announcement.objects.create(
        title=title,
        content=content,
        status=status,
    )


@transaction.atomic
def update_announcement(
    announcement: Announcement,
    *,
    title,
    content,
    status,
) -> Announcement:
    announcement.title = title
    announcement.content = content
    announcement.status = status
    announcement.save(
        update_fields=[
            "title",
            "content",
            "status",
            "updated_at",
        ]
    )
    return announcement


@transaction.atomic
def publish_announcement(
    announcement: Announcement,
) -> Announcement:
    from django.utils import timezone

    announcement.status = AnnouncementStatus.PUBLISHED

    if announcement.published_at is None:
        announcement.published_at = timezone.now()

    announcement.save(
        update_fields=[
            "status",
            "published_at",
            "updated_at",
        ]
    )

    return announcement


@transaction.atomic
def archive_announcement(
    announcement: Announcement,
) -> Announcement:
    announcement.status = AnnouncementStatus.ARCHIVED

    announcement.save(
        update_fields=[
            "status",
            "updated_at",
        ]
    )

    return announcement


# ============================================================================
# Contact Message Services
# ============================================================================

@transaction.atomic
def create_contact_message(
    *,
    name,
    email,
    subject,
    message,
) -> ContactMessage:
    return ContactMessage.objects.create(
        name=name,
        email=email,
        subject=subject,
        message=message,
    )


@transaction.atomic
def update_contact_message(
    contact_message: ContactMessage,
    *,
    status,
) -> ContactMessage:
    contact_message.status = status

    contact_message.save(
        update_fields=[
            "status",
            "updated_at",
        ]
    )

    return contact_message


@transaction.atomic
def mark_contact_message_in_progress(
    contact_message: ContactMessage,
) -> ContactMessage:
    contact_message.status = MessageStatus.IN_PROGRESS

    contact_message.save(
        update_fields=[
            "status",
            "updated_at",
        ]
    )

    return contact_message


@transaction.atomic
def resolve_contact_message(
    contact_message: ContactMessage,
) -> ContactMessage:
    contact_message.status = MessageStatus.RESOLVED

    contact_message.save(
        update_fields=[
            "status",
            "updated_at",
        ]
    )

    return contact_message


# ============================================================================
# FAQ Services
# ============================================================================

@transaction.atomic
def create_faq(
    *,
    question,
    answer,
    is_active=True,
    display_order=0,
) -> FAQ:
    return FAQ.objects.create(
        question=question,
        answer=answer,
        is_active=is_active,
        display_order=display_order,
    )


@transaction.atomic
def update_faq(
    faq: FAQ,
    *,
    question,
    answer,
    is_active,
    display_order,
) -> FAQ:
    faq.question = question
    faq.answer = answer
    faq.is_active = is_active
    faq.display_order = display_order

    faq.save(
        update_fields=[
            "question",
            "answer",
            "is_active",
            "display_order",
            "updated_at",
        ]
    )

    return faq


@transaction.atomic
def activate_faq(
    faq: FAQ,
) -> FAQ:
    faq.is_active = True

    faq.save(
        update_fields=[
            "is_active",
            "updated_at",
        ]
    )

    return faq


@transaction.atomic
def deactivate_faq(
    faq: FAQ,
) -> FAQ:
    faq.is_active = False

    faq.save(
        update_fields=[
            "is_active",
            "updated_at",
        ]
    )

    return faq


# ============================================================================
# Newsletter Services
# ============================================================================

@transaction.atomic
def create_newsletter(
    *,
    email,
) -> Newsletter:
    return Newsletter.objects.create(
        email=email,
    )


@transaction.atomic
def activate_newsletter(
    newsletter: Newsletter,
) -> Newsletter:
    newsletter.is_active = True

    newsletter.save(
        update_fields=[
            "is_active",
            "updated_at",
        ]
    )

    return newsletter


@transaction.atomic
def deactivate_newsletter(
    newsletter: Newsletter,
) -> Newsletter:
    newsletter.is_active = False

    newsletter.save(
        update_fields=[
            "is_active",
            "updated_at",
        ]
    )

    return newsletter