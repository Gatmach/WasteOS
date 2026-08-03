
from django.db import models

from apps.common.models import BaseModel

from .collection_route import CollectionRoute
from .collection_vehicle import CollectionVehicle
from .driver import Driver
from apps.operations.choices import ScheduleStatus

class CollectionSchedule(BaseModel):

    route = models.ForeignKey(
        CollectionRoute,
        on_delete=models.CASCADE,
        related_name="schedules",
    )

    vehicle = models.ForeignKey(
        CollectionVehicle,
        on_delete=models.CASCADE,
        related_name="schedules",
    )

    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        related_name="schedules",
    )

    scheduled_date = models.DateField()

    scheduled_time = models.TimeField()

    status = models.CharField(
        max_length=30,
        choices=ScheduleStatus.choices,
        default=ScheduleStatus.PENDING,
    )

    class Meta:
        ordering = ["scheduled_date", "scheduled_time"]

    def __str__(self):
        return f"{self.route} ({self.scheduled_date})"