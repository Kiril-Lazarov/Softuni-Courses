from django.contrib import admin

from photo_gallery.photos.models import PhotoComments, AstroPhotographyAssessment, PortraitPhotographyAssessment, \
    StreetPhotographyAssessment


@admin.register(PhotoComments)
class PhotoCommentsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user_id', 'photo_id', 'comment',)


@admin.register(AstroPhotographyAssessment)
class AstroPhotographyAssessmentAdmin(admin.ModelAdmin):
    pass


@admin.register(PortraitPhotographyAssessment)
class PortraitPhotographyAssessment(admin.ModelAdmin):
    pass

@admin.register(StreetPhotographyAssessment)
class StreetPhotographyAssessment(admin.ModelAdmin):
    pass