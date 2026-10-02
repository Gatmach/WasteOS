
from rest_framework.routers import DefaultRouter

from apps.website.api import (
    AnnouncementViewSet,
    ContactMessageViewSet,
    FAQViewSet,
    NewsletterViewSet,
)

router = DefaultRouter()

router.register(
    r"announcements",
    AnnouncementViewSet,
    basename="announcement",
)

router.register(
    r"contact-messages",
    ContactMessageViewSet,
    basename="contact-message",
)

router.register(
    r"faqs",
    FAQViewSet,
    basename="faq",
)

router.register(
    r"newsletters",
    NewsletterViewSet,
    basename="newsletter",
)

urlpatterns = router.urls