
from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if value and len(value) < 10:
        raise ValidationError("Phone number is too short.")