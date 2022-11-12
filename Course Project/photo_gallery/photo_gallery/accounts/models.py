from enum import Enum

from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from photo_gallery.accounts.validators import validate_chars

class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name,x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())

class Gender(ChoicesEnumMixin,Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not show'




class AppUser(auth_models.AbstractUser):
    MAX_LEN_FIRST_NAME = 30
    MIX_LEN_FIRST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MIX_LEN_LAST_NAME = 2



    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(validators.MinLengthValidator(MIX_LEN_LAST_NAME),validate_chars),
    )
    last_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(validators.MinLengthValidator(MIX_LEN_LAST_NAME),validate_chars)
    )
    email = models.EmailField(
        null=True,
        blank=True,
        unique=True,
    )

    gender = models.CharField(
        max_length=Gender.max_len(),
        choices=Gender.choices(),
    )
