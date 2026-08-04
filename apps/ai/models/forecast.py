
from django.db import models

from apps.common.models import BaseModel
from apps.bins.models import SmartBin


class Forecast(BaseModel):
    smart_bin = models.ForeignKey(
        SmartBin,
        on_delete=models.CASCADE,
        related_name="forecasts",
    )

    forecast_date = models.DateField()

    expected_fill_level = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    class Meta:
        ordering = ["forecast_date"]

    def __str__(self):
        return (
            f"{self.smart_bin} - "
            f"{self.forecast_date}"
        )