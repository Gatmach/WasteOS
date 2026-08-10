from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.notifications.api import (
    CreateNotificationSerializer,
    NotificationSerializer,
)
from apps.notifications.selectors import (
    get_notification,
    get_unread_notification_count,
    get_unread_notifications,
    get_user_notifications,
)
from apps.notifications.services import (
    create_notification,
    mark_all_notifications_as_read,
    mark_notification_as_read,
)


class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = get_user_notifications(
            request.user,
        )

        serializer = NotificationSerializer(
            notifications,
            many=True,
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = CreateNotificationSerializer(
            data=request.data,
        )

        serializer.is_valid(raise_exception=True)

        notification = create_notification(
            user=request.user,
            **serializer.validated_data,
        )

        return Response(
            NotificationSerializer(notification).data,
            status=status.HTTP_201_CREATED,
        )


class UnreadNotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = get_unread_notifications(
            request.user,
        )

        serializer = NotificationSerializer(
            notifications,
            many=True,
        )

        return Response(serializer.data)


class UnreadNotificationCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        count = get_unread_notification_count(
            request.user,
        )

        return Response(
            {
                "count": count,
            }
        )


class NotificationDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, notification_id):
        notification = get_notification(
            notification_id,
            request.user,
        )

        if notification is None:
            return Response(
                {
                    "detail": "Notification not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = NotificationSerializer(
            notification,
        )

        return Response(serializer.data)


class MarkNotificationReadView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, notification_id):
        notification = get_notification(
            notification_id,
            request.user,
        )

        if notification is None:
            return Response(
                {
                    "detail": "Notification not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        notification = mark_notification_as_read(
            notification=notification,
        )

        return Response(
            NotificationSerializer(notification).data,
        )


class MarkAllNotificationsReadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        updated_count = mark_all_notifications_as_read(
            user=request.user,
        )

        return Response(
            {
                "updated_count": updated_count,
            }
        )