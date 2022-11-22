from enum import Enum

from django.core import validators
from django.db import models
from django.db.models.signals import pre_save

from photo_gallery.accounts.models import AppUser, ChoicesEnumMixin
from photo_gallery.utils import unique_slug_generator

#
class Ratings(ChoicesEnumMixin, Enum):
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    six = '6'


class PhotoCategory(ChoicesEnumMixin, Enum):
    astro_photography = 'Astro photography'
    portrait = 'Portrait'
    street = 'Street'


class BasePhotos(models.Model):
    MAX_LEN_TITLE = 250
    MIN_LEN_TITLE = 2
    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        validators=(validators.MinLengthValidator(MIN_LEN_TITLE),),

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
    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    published_date = models.DateTimeField(
        auto_now_add=True,
    )

    category = models.CharField(
        max_length=PhotoCategory.max_len(),
        choices=PhotoCategory.choices(),
    )


class PhotoComments(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
    )

    photo = models.OneToOneField(
        BasePhotos,
        on_delete=models.CASCADE,
    )

    comment = models.TextField(
        null=True,
        blank=True,
    )
    published_date = models.DateTimeField(
        auto_now_add=True,
    )


def slug_generator(sender, instance, *args, **kwargs):
    instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=BasePhotos)


class AstroPhotographyAssessment(models.Model):
    MIN_ASSESSMENT = 0

    photo = models.ForeignKey(
        BasePhotos,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    rating1 = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=(validators.MaxValueValidator(10),),

    )

    light = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )
    focus = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )
    detail = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )
    contrast = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )
    color_temperature = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
        verbose_name='Color Temperature',
    )

class PortraitPhotographyAssessment(models.Model):
    MIN_ASSESSMENT = 0

    photo = models.ForeignKey(
        BasePhotos,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    rating1 = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
    )
    light = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )
    focus = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )
    contrast = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )

    emotion = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )

    creativity = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )
    composition = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )




class StreetPhotographyAssessment(models.Model):
    MIN_ASSESSMENT = 0

    photo = models.ForeignKey(
        BasePhotos,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    rating1 = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
    )

    light = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )
    focus = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )
    contrast = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )
    story_line = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
        verbose_name='Story Line'
    )
    emotion = models.IntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        choices=Ratings.choices(),
    )


