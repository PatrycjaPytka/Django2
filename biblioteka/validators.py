from django.core.exceptions import ValidationError


def validate_rok(value):
    if value > 2020:
        raise ValidationError("Rok jest większy niż 2020")
    return value