from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.accounts.models import User
from apps.notifications.choices import (
    NotificationChannel,
    NotificationType,
)
from apps.notifications.models import (
    Notification,
    NotificationLog,
)


class NotificationAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="notification_user",
            email="notification@example.com",
            password="TestPassword123!",
            phone_number="+2547000001",
        )

        self.other_user = User.objects.create_user(
            username="other_user",
            email="other@example.com",
            password="TestPassword123!",
            phone_number="+2547000002",
        )

        self.client.force_authenticate(
            user=self.user,
        )

        self.notification = Notification.objects.create(
            user=self.user,
            title="Bin Full",
            message="Bin BIN-001 is full.",
            notification_type=NotificationType.ALERT,
            channel=NotificationChannel.IN_APP,
        )

        self.unread_notification = Notification.objects.create(
            user=self.user,
            title="Collection Reminder",
            message="Collection scheduled for tomorrow.",
            notification_type=NotificationType.REMINDER,
            channel=NotificationChannel.IN_APP,
        )

        self.other_notification = Notification.objects.create(
            user=self.other_user,
            title="Private Notification",
            message="This belongs to another user.",
            notification_type=NotificationType.SYSTEM,
            channel=NotificationChannel.IN_APP,
        )

    def test_notification_list(self):
        url = reverse("notification-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data),
            2,
        )

    def test_create_notification(self):
        url = reverse("notification-list")

        payload = {
            "title": "System Update",
            "message": "WasteOS has been updated.",
            "notification_type": NotificationType.SYSTEM,
            "channel": NotificationChannel.IN_APP,
        }

        response = self.client.post(
            url,
            payload,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

        self.assertEqual(
            Notification.objects.filter(
                user=self.user,
            ).count(),
            3,
        )

    def test_unread_notifications(self):
        url = reverse(
            "notification-unread-list",
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data),
            2,
        )

    def test_unread_notification_count(self):
        url = reverse(
            "notification-unread-count",
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["count"],
            2,
        )

    def test_notification_detail(self):
        url = reverse(
            "notification-detail",
            kwargs={
                "notification_id": self.notification.id,
            },
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["id"],
            str(self.notification.id),
        )

    def test_user_cannot_access_other_users_notification(self):
        url = reverse(
            "notification-detail",
            kwargs={
                "notification_id": self.other_notification.id,
            },
        )

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_mark_notification_as_read(self):
        url = reverse(
            "notification-mark-read",
            kwargs={
                "notification_id": self.notification.id,
            },
        )

        response = self.client.patch(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.notification.refresh_from_db()

        self.assertTrue(
            self.notification.is_read,
        )

    def test_mark_all_notifications_as_read(self):
        url = reverse(
            "notification-mark-all-read",
        )

        response = self.client.post(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["updated_count"],
            2,
        )

        self.assertEqual(
            Notification.objects.filter(
                user=self.user,
                is_read=False,
            ).count(),
            0,
        )

class NotificationServiceTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="service_user",
            email="service@example.com",
            password="TestPassword123!",
        )

        self.notification = Notification.objects.create(
            user=self.user,
            title="Bin Alert",
            message="Bin BIN-001 is full.",
            notification_type=NotificationType.ALERT,
            channel=NotificationChannel.IN_APP,
        )

    def test_create_notification_log(self):
        from apps.notifications.services import (
            create_notification_log,
        )

        log = create_notification_log(
            notification=self.notification,
            response="Delivered successfully.",
            is_successful=True,
        )

        self.assertIsInstance(
            log,
            NotificationLog,
        )

        self.assertEqual(
            log.notification,
            self.notification,
        )

        self.assertEqual(
            log.response,
            "Delivered successfully.",
        )

        self.assertTrue(
            log.is_successful,
        )

    def test_send_in_app_notification(self):
        from apps.notifications.services import (
            send_notification,
        )

        log = send_notification(
            notification=self.notification,
        )

        self.assertTrue(
            log.is_successful,
        )

        self.assertEqual(
            log.notification,
            self.notification,
        )

        self.assertEqual(
            NotificationLog.objects.filter(
                notification=self.notification,
            ).count(),
            1,
        )

    def test_send_unsupported_channel_fails(self):
        from apps.notifications.services import (
            send_notification,
        )

        self.notification.channel = NotificationChannel.EMAIL
        self.notification.save(
            update_fields=[
                "channel",
                "updated_at",
            ]
        )

        log = send_notification(
            notification=self.notification,
        )

        self.assertFalse(
            log.is_successful,
        )

        self.assertIn(
            "not configured",
            log.response,
        )