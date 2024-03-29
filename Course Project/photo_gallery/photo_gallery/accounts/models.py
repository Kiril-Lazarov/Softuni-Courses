from enum import Enum

import django.contrib.auth.validators
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
        return max(len(name) for name,_  in cls.choices()) + 2

class Gender(ChoicesEnumMixin,Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not show'




class AppUser(auth_models.AbstractUser):
    MAX_LEN_FIRST_NAME = 30
    MIX_LEN_FIRST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MIX_LEN_LAST_NAME = 2

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()]
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_FIRST_NAME,
        validators=(validators.MinLengthValidator(MIX_LEN_LAST_NAME),validate_chars),
        verbose_name='First Name'
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_FIRST_NAME,
        validators=(validators.MinLengthValidator(MIX_LEN_LAST_NAME),validate_chars),
        verbose_name = 'Last Name',

    )
    email = models.EmailField(

        unique=True,
    )

    gender = models.CharField(
        # null=True,
        # blank=True,
        max_length=Gender.max_len(),
        choices=Gender.choices(),
        default='Do not show',
    )

    profile_picture = models.ImageField(
        null=True,
        blank=True,
        upload_to='media_files/profile_pictures',
    )

    about_me = models.TextField(
        null=True,
        blank=True,
    )