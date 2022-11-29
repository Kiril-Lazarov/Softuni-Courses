from enum import Enum

from django.core import validators
from django.db import models
from django.db.models.signals import pre_save

from photo_gallery.accounts.models import AppUser, ChoicesEnumMixin
from photo_gallery.utils import unique_slug_generator


class PhotoCategory(ChoicesEnumMixin, Enum):
    astro_photography = 'Astro photography'
    portrait = 'Portrait'
    street = 'Street'


class BasePhotos(models.Model):
    MAX_LEN_TITLE = 250
    MIN_LEN_TITLE = 2

    class Meta:
        verbose_name_plural = 'Base Photos'

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
    class Meta:
        verbose_name_plural = 'Photo Comments'

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
    MAX_ASSESSMENT = 6

    photo = models.ForeignKey(
        BasePhotos,
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )
    assessing_user = models.IntegerField(
        null=True,
        blank=True,
    )

    rating1 = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(10),),

    )

    light = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )
    focus = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )
    detail = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )
    contrast = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )
    color_temperature = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
        verbose_name='Color Temperature',
    )



class PortraitPhotographyAssessment(models.Model):
    MIN_ASSESSMENT = 0
    MAX_ASSESSMENT = 6

    photo = models.ForeignKey(
        BasePhotos,
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )
    assessing_user = models.IntegerField(
        null=True,
        blank=True,
    )

    rating1 = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
    )
    light = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )
    focus = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )
    contrast = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )

    emotion = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )

    creativity = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )
    composition = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )


class StreetPhotographyAssessment(models.Model):
    MIN_ASSESSMENT = 0
    MAX_ASSESSMENT = 6

    photo = models.ForeignKey(
        BasePhotos,
        on_delete=models.CASCADE,
    )
    owner = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )
    assessing_user = models.IntegerField(
        null=True,
        blank=True,
    )

    rating1 = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=MIN_ASSESSMENT,
    )

    light = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )
    focus = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )
    contrast = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )
    story_line = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
        verbose_name='Story Line'
    )
    emotion = models.PositiveIntegerField(
        default=MIN_ASSESSMENT,
        validators=(validators.MaxValueValidator(MAX_ASSESSMENT),),
    )
