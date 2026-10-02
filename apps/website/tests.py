
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()

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
from apps.website.services import (
    activate_faq,
    activate_newsletter,
    archive_announcement,
    create_announcement,
    create_contact_message,
    create_faq,
    create_newsletter,
    deactivate_faq,
    deactivate_newsletter,
    mark_contact_message_in_progress,
    publish_announcement,
    resolve_contact_message,
    update_announcement,
    update_contact_message,
    update_faq,
)


class AnnouncementServiceTests(TestCase):

    def test_create_announcement(self):
        announcement = create_announcement(
            title="System Maintenance",
            content="WasteOS will undergo scheduled maintenance.",
        )

        self.assertEqual(announcement.title, "System Maintenance")
        self.assertEqual(
            announcement.status,
            AnnouncementStatus.DRAFT,
        )
        self.assertIsNone(announcement.published_at)

    def test_update_announcement(self):
        announcement = Announcement.objects.create(
            title="Old Title",
            content="Old content",
        )

        updated = update_announcement(
            announcement,
            title="New Title",
            content="New content",
            status=AnnouncementStatus.PUBLISHED,
        )

        self.assertEqual(updated.title, "New Title")
        self.assertEqual(updated.content, "New content")
        self.assertEqual(
            updated.status,
            AnnouncementStatus.PUBLISHED,
        )

    def test_publish_announcement(self):
        announcement = Announcement.objects.create(
            title="System Update",
            content="New system update.",
        )

        published = publish_announcement(announcement)

        self.assertEqual(
            published.status,
            AnnouncementStatus.PUBLISHED,
        )
        self.assertIsNotNone(published.published_at)

    def test_archive_announcement(self):
        announcement = Announcement.objects.create(
            title="Old Announcement",
            content="Old content.",
            status=AnnouncementStatus.PUBLISHED,
        )

        archived = archive_announcement(announcement)

        self.assertEqual(
            archived.status,
            AnnouncementStatus.ARCHIVED,
        )


class ContactMessageServiceTests(TestCase):

    def test_create_contact_message(self):
        contact_message = create_contact_message(
            name="John Doe",
            email="john@example.com",
            subject="Waste collection issue",
            message="My area has not been collected.",
        )

        self.assertEqual(contact_message.name, "John Doe")
        self.assertEqual(contact_message.email, "john@example.com")
        self.assertEqual(
            contact_message.status,
            MessageStatus.NEW,
        )

    def test_update_contact_message(self):
        contact_message = ContactMessage.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            subject="Test",
            message="Test message.",
        )

        updated = update_contact_message(
            contact_message,
            status=MessageStatus.IN_PROGRESS,
        )

        self.assertEqual(
            updated.status,
            MessageStatus.IN_PROGRESS,
        )

    def test_mark_contact_message_in_progress(self):
        contact_message = ContactMessage.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            subject="Test",
            message="Test message.",
        )

        updated = mark_contact_message_in_progress(contact_message)

        self.assertEqual(
            updated.status,
            MessageStatus.IN_PROGRESS,
        )

    def test_resolve_contact_message(self):
        contact_message = ContactMessage.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            subject="Test",
            message="Test message.",
        )

        resolved = resolve_contact_message(contact_message)

        self.assertEqual(
            resolved.status,
            MessageStatus.RESOLVED,
        )


class FAQServiceTests(TestCase):

    def test_create_faq(self):
        faq = create_faq(
            question="How does WasteOS work?",
            answer="WasteOS manages smart waste collection.",
        )

        self.assertEqual(
            faq.question,
            "How does WasteOS work?",
        )
        self.assertEqual(faq.answer, "WasteOS manages smart waste collection.")
        self.assertTrue(faq.is_active)
        self.assertEqual(faq.display_order, 0)

    def test_update_faq(self):
        faq = FAQ.objects.create(
            question="Old question",
            answer="Old answer",
        )

        updated = update_faq(
            faq,
            question="New question",
            answer="New answer",
            is_active=False,
            display_order=2,
        )

        self.assertEqual(updated.question, "New question")
        self.assertEqual(updated.answer, "New answer")
        self.assertFalse(updated.is_active)
        self.assertEqual(updated.display_order, 2)

    def test_activate_faq(self):
        faq = FAQ.objects.create(
            question="Test question",
            answer="Test answer",
            is_active=False,
        )

        activated = activate_faq(faq)

        self.assertTrue(activated.is_active)

    def test_deactivate_faq(self):
        faq = FAQ.objects.create(
            question="Test question",
            answer="Test answer",
            is_active=True,
        )

        deactivated = deactivate_faq(faq)

        self.assertFalse(deactivated.is_active)


class NewsletterServiceTests(TestCase):

    def test_create_newsletter(self):
        newsletter = create_newsletter(
            email="subscriber@example.com",
        )

        self.assertEqual(
            newsletter.email,
            "subscriber@example.com",
        )
        self.assertTrue(newsletter.is_active)

    def test_activate_newsletter(self):
        newsletter = Newsletter.objects.create(
            email="subscriber@example.com",
            is_active=False,
        )

        activated = activate_newsletter(newsletter)

        self.assertTrue(activated.is_active)

    def test_deactivate_newsletter(self):
        newsletter = Newsletter.objects.create(
            email="subscriber@example.com",
            is_active=True,
        )

        deactivated = deactivate_newsletter(newsletter)

        self.assertFalse(deactivated.is_active)

class AnnouncementAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="website_admin",
            email="admin@example.com",
            password="TestPassword123!",
        )

        self.client.force_authenticate(
            user=self.user,
        )

    def test_list_announcements_returns_200(self):
        Announcement.objects.create(
            title="System Maintenance",
            content="Scheduled maintenance.",
        )

        url = reverse("announcement-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_create_announcement(self):
        url = reverse("announcement-list")

        data = {
            "title": "New Announcement",
            "content": "WasteOS has a new update.",
            "status": AnnouncementStatus.DRAFT,
        }

        response = self.client.post(
            url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            response.data["title"],
            "New Announcement",
        )

        self.assertTrue(
            Announcement.objects.filter(
                title="New Announcement",
            ).exists()
        )

    def test_update_announcement(self):
        announcement = Announcement.objects.create(
            title="Old Title",
            content="Old content.",
        )

        url = reverse(
            "announcement-detail",
            kwargs={"pk": announcement.pk},
        )

        data = {
            "title": "Updated Title",
            "content": "Updated content.",
            "status": AnnouncementStatus.PUBLISHED,
        }

        response = self.client.put(
            url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        announcement.refresh_from_db()

        self.assertEqual(
            announcement.title,
            "Updated Title",
        )

        self.assertEqual(
            announcement.content,
            "Updated content.",
        )

    def test_published_endpoint_is_public(self):
        Announcement.objects.create(
            title="Published Announcement",
            content="Public announcement.",
            status=AnnouncementStatus.PUBLISHED,
        )

        self.client.force_authenticate(user=None)

        url = reverse("announcement-published")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_published_endpoint_returns_only_published(self):
        Announcement.objects.create(
            title="Published",
            content="Published content.",
            status=AnnouncementStatus.PUBLISHED,
        )

        Announcement.objects.create(
            title="Draft",
            content="Draft content.",
            status=AnnouncementStatus.DRAFT,
        )

        self.client.force_authenticate(user=None)

        url = reverse("announcement-published")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        results = response.data["results"]

        self.assertEqual(
            len(results),
            1,
        )

        self.assertEqual(
            results[0]["title"],
            "Published",
        )

    def test_publish_action(self):
        announcement = Announcement.objects.create(
            title="Draft Announcement",
            content="Draft content.",
            status=AnnouncementStatus.DRAFT,
        )

        url = reverse(
            "announcement-publish",
            kwargs={"pk": announcement.pk},
        )

        response = self.client.post(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        announcement.refresh_from_db()

        self.assertEqual(
            announcement.status,
            AnnouncementStatus.PUBLISHED,
        )

        self.assertIsNotNone(
            announcement.published_at,
        )

    def test_archive_action(self):
        announcement = Announcement.objects.create(
            title="Published Announcement",
            content="Published content.",
            status=AnnouncementStatus.PUBLISHED,
        )

        url = reverse(
            "announcement-archive",
            kwargs={"pk": announcement.pk},
        )

        response = self.client.post(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        announcement.refresh_from_db()

        self.assertEqual(
            announcement.status,
            AnnouncementStatus.ARCHIVED,
        )


class ContactMessageAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="contact_admin",
            email="contact-admin@example.com",
            password="TestPassword123!",
        )

        self.client.force_authenticate(
            user=self.user,
        )

    def test_list_contact_messages_returns_200(self):
        ContactMessage.objects.create(
            name="John Doe",
            email="john@example.com",
            subject="Waste collection issue",
            message="My area was not collected.",
        )

        url = reverse("contact-message-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_create_contact_message_is_public(self):
        self.client.force_authenticate(user=None)

        url = reverse("contact-message-list")

        data = {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "subject": "Collection request",
            "message": "Please collect waste from our area.",
        }

        response = self.client.post(
            url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertTrue(
            ContactMessage.objects.filter(
                email="jane@example.com",
            ).exists()
        )

    def test_unauthenticated_list_is_rejected(self):
        self.client.force_authenticate(user=None)

        url = reverse("contact-message-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_update_contact_message(self):
        contact_message = ContactMessage.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            subject="Test",
            message="Test message.",
        )

        url = reverse(
            "contact-message-detail",
            kwargs={"pk": contact_message.pk},
        )

        response = self.client.patch(
            url,
            {
                "status": MessageStatus.IN_PROGRESS,
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        contact_message.refresh_from_db()

        self.assertEqual(
            contact_message.status,
            MessageStatus.IN_PROGRESS,
        )

    def test_mark_in_progress_action(self):
        contact_message = ContactMessage.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            subject="Test",
            message="Test message.",
        )

        url = reverse(
            "contact-message-mark-in-progress",
            kwargs={"pk": contact_message.pk},
        )

        response = self.client.post(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        contact_message.refresh_from_db()

        self.assertEqual(
            contact_message.status,
            MessageStatus.IN_PROGRESS,
        )

    def test_resolve_action(self):
        contact_message = ContactMessage.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            subject="Test",
            message="Test message.",
        )

        url = reverse(
            "contact-message-resolve",
            kwargs={"pk": contact_message.pk},
        )

        response = self.client.post(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        contact_message.refresh_from_db()

        self.assertEqual(
            contact_message.status,
            MessageStatus.RESOLVED,
        )

class FAQAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="faq_admin",
            email="faq-admin@example.com",
            password="TestPassword123!",
        )

        self.client.force_authenticate(
            user=self.user,
        )

    def test_list_faqs_returns_200(self):
        FAQ.objects.create(
            question="How does WasteOS work?",
            answer="WasteOS manages smart waste collection.",
        )

        url = reverse("faq-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_create_faq(self):
        url = reverse("faq-list")

        data = {
            "question": "What is WasteOS?",
            "answer": "WasteOS is a smart waste management platform.",
            "is_active": True,
            "display_order": 1,
        }

        response = self.client.post(
            url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            response.data["question"],
            "What is WasteOS?",
        )

        self.assertTrue(
            FAQ.objects.filter(
                question="What is WasteOS?",
            ).exists()
        )

    def test_update_faq(self):
        faq = FAQ.objects.create(
            question="Old question",
            answer="Old answer.",
        )

        url = reverse(
            "faq-detail",
            kwargs={"pk": faq.pk},
        )

        data = {
            "question": "Updated question",
            "answer": "Updated answer.",
            "is_active": False,
            "display_order": 3,
        }

        response = self.client.put(
            url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        faq.refresh_from_db()

        self.assertEqual(
            faq.question,
            "Updated question",
        )

        self.assertFalse(
            faq.is_active,
        )

        self.assertEqual(
            faq.display_order,
            3,
        )

    def test_active_endpoint_is_public(self):
        FAQ.objects.create(
            question="Active FAQ",
            answer="Active answer.",
            is_active=True,
        )

        self.client.force_authenticate(user=None)

        url = reverse("faq-active")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_active_endpoint_returns_only_active_faqs(self):
        FAQ.objects.create(
            question="Active FAQ",
            answer="Active answer.",
            is_active=True,
        )

        FAQ.objects.create(
            question="Inactive FAQ",
            answer="Inactive answer.",
            is_active=False,
        )

        self.client.force_authenticate(user=None)

        url = reverse("faq-active")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        results = response.data["results"]

        self.assertEqual(
            len(results),
            1,
        )

        self.assertEqual(
            results[0]["question"],
            "Active FAQ",
        )

    def test_activate_action(self):
        faq = FAQ.objects.create(
            question="Inactive FAQ",
            answer="Answer.",
            is_active=False,
        )

        url = reverse(
            "faq-activate",
            kwargs={"pk": faq.pk},
        )

        response = self.client.post(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        faq.refresh_from_db()

        self.assertTrue(
            faq.is_active,
        )

    def test_deactivate_action(self):
        faq = FAQ.objects.create(
            question="Active FAQ",
            answer="Answer.",
            is_active=True,
        )

        url = reverse(
            "faq-deactivate",
            kwargs={"pk": faq.pk},
        )

        response = self.client.post(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        faq.refresh_from_db()

        self.assertFalse(
            faq.is_active,
        )

class NewsletterAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="newsletter_admin",
            email="newsletter-admin@example.com",
            password="TestPassword123!",
        )

        self.client.force_authenticate(
            user=self.user,
        )

    def test_list_newsletters_returns_200(self):
        Newsletter.objects.create(
            email="subscriber@example.com",
        )

        url = reverse("newsletter-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_create_newsletter_is_public(self):
        self.client.force_authenticate(user=None)

        url = reverse("newsletter-list")

        data = {
            "email": "newsubscriber@example.com",
        }

        response = self.client.post(
            url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertTrue(
            Newsletter.objects.filter(
                email="newsubscriber@example.com",
            ).exists()
        )

    def test_unauthenticated_list_is_rejected(self):
        self.client.force_authenticate(user=None)

        url = reverse("newsletter-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_active_endpoint_is_public(self):
        Newsletter.objects.create(
            email="active@example.com",
            is_active=True,
        )

        self.client.force_authenticate(user=None)

        url = reverse("newsletter-active")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_active_endpoint_returns_only_active_newsletters(self):
        Newsletter.objects.create(
            email="active@example.com",
            is_active=True,
        )

        Newsletter.objects.create(
            email="inactive@example.com",
            is_active=False,
        )

        self.client.force_authenticate(user=None)

        url = reverse("newsletter-active")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        results = response.data["results"]

        self.assertEqual(
            len(results),
            1,
        )

        self.assertEqual(
            results[0]["email"],
            "active@example.com",
        )

    def test_activate_action(self):
        newsletter = Newsletter.objects.create(
            email="subscriber@example.com",
            is_active=False,
        )

        url = reverse(
            "newsletter-activate",
            kwargs={"pk": newsletter.pk},
        )

        response = self.client.post(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        newsletter.refresh_from_db()

        self.assertTrue(
            newsletter.is_active,
        )

    def test_deactivate_action(self):
        newsletter = Newsletter.objects.create(
            email="subscriber@example.com",
            is_active=True,
        )

        url = reverse(
            "newsletter-deactivate",
            kwargs={"pk": newsletter.pk},
        )

        response = self.client.post(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        newsletter.refresh_from_db()

        self.assertFalse(
            newsletter.is_active,
        )