
from apps.operations.models import Driver
from django.db import transaction

# ============================================================================
# Driver Services
# ============================================================================

@transaction.atomic
def create_driver(**validated_data) -> Driver:
    return Driver.objects.create(**validated_data)


@transaction.atomic
def update_driver(
    driver: Driver,
    **validated_data,
) -> Driver:
    for field, value in validated_data.items():
        setattr(driver, field, value)

    driver.save()

    return driver


@transaction.atomic
def activate_driver(driver: Driver) -> Driver:
    driver.is_active = True
    driver.save(update_fields=["is_active"])

    return driver


@transaction.atomic
def deactivate_driver(driver: Driver) -> Driver:
    driver.is_active = False
    driver.save(update_fields=["is_active"])

    return driver