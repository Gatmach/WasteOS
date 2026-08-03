from django.db import models


class FacilityType(models.TextChoices):
    UNIVERSITY = "university", "University"
    HOSPITAL = "hospital", "Hospital"
    MARKET = "market", "Market"
    OFFICE = "office", "Office"
    RESIDENTIAL = "residential", "Residential"
    INDUSTRIAL = "industrial", "Industrial"
    OTHER = "other", "Other"