from django import forms

from photo_gallery.photos.models import AstroPhotographyAssessment, PortraitPhotographyAssessment, \
    StreetPhotographyAssessment


class AstroPhotographyAssessmentForm(forms.ModelForm):
    class Meta:
        model = AstroPhotographyAssessment
        exclude = ('_state', 'id', 'photo_id', 'user_id', 'rating1', 'photo', 'user')


class PortraitPhotographyAssessmentForm(forms.ModelForm):
    class Meta:
        model = PortraitPhotographyAssessment
        exclude = ('_state', 'id', 'photo_id', 'user_id', 'rating1', 'photo', 'user')


class StreetPhotographyAssessmentForm(forms.ModelForm):
    class Meta:
        model = StreetPhotographyAssessment
        exclude = ('_state', 'id', 'photo_id', 'user_id', 'rating1', 'photo', 'user')