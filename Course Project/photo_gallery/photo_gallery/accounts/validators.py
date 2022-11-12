from django.core.exceptions import ValidationError


def validate_chars(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Name must content only letters.')