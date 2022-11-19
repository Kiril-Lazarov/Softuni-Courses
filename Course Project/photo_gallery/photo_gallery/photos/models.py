from django.core import validators
from django.db import models


class BasePhotos(models.Model):
    MAX_LEN_TITLE = 50
    MIN_LEN_TITLE = 2
    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        validators=(validators.MinLengthValidator(MIN_LEN_TITLE),),
        unique=True,
    )

    image = models.ImageField(
        upload_to='photos',
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(

    )
