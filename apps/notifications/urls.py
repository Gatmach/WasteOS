
from django.urls import path

from apps.notifications.views import (
    MarkAllNotificationsReadView,
    MarkNotificationReadView,
    NotificationDetailView,
    NotificationListView,
    UnreadNotificationCountView,
    UnreadNotificationListView,
)


urlpatterns = [
    path(
        "",
        NotificationListView.as_view(),
        name="notification-list",
    ),

    path(
        "unread/",
        UnreadNotificationListView.as_view(),
        name="notification-unread-list",
    ),

    path(
        "unread-count/",
        UnreadNotificationCountView.as_view(),
        name="notification-unread-count",
    ),

    path(
        "mark-all-read/",
        MarkAllNotificationsReadView.as_view(),
        name="notification-mark-all-read",
    ),

    path(
        "<uuid:notification_id>/",
        NotificationDetailView.as_view(),
        name="notification-detail",
    ),

    path(
        "<uuid:notification_id>/read/",
        MarkNotificationReadView.as_view(),
        name="notification-mark-read",
    ),
]