
from django.db.models import QuerySet

from apps.operations.models import Driver
from django.db.models import Q

# ============================================================================
# Driver Selectors
# ============================================================================

def get_driver(driver_id) -> Driver:
    return Driver.objects.get(pk=driver_id)


def list_drivers() -> QuerySet[Driver]:
    return Driver.objects.all()


def get_active_drivers() -> QuerySet[Driver]:
    return Driver.objects.filter(is_active=True)


def search_drivers(query) -> QuerySet[Driver]:
    return Driver.objects.filter(
        Q(first_name__icontains=query),
    ) | Driver.objects.filter(
        Q(last_name__icontains=query),
    ) | Driver.objects.filter(
        Q(phone_number__icontains=query),
    ) | Driver.objects.filter(
        Q(license_number__icontains=query),
    )