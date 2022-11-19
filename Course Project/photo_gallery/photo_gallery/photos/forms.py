from django import forms

from photo_gallery.photos.models import BasePhotos, AstroPhotographyAssessment

photo_models = {
    'astro_photography': AstroPhotographyAssessment
}


class UploadPhotoForm(forms.ModelForm):
    class Meta:
        model = BasePhotos
        exclude = ('slug', 'user')



class UploadAstroPhotoForm(forms.ModelForm):
    class Meta:
        model = AstroPhotographyAssessment
        fields = ('rating1',)

    @classmethod
    def get_model(cls):
        if __name__ == '__main__':
            return AstroPhotographyAssessment


class EditPhotoForm(forms.ModelForm):
    class Meta:
        model = BasePhotos
        exclude = ('slug',)


class DeletePhotoForm(forms.ModelForm):
    class Meta:
        model = BasePhotos
        exclude = ('title', 'image', 'description', 'slug', 'user', 'published_date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].required = False

    def save(self, commit=True):
        if commit:
            photo_category = self.instance.category
            photo_id = self.instance.pk
            photo_models[photo_category].objects.filter(photo_id=photo_id).get().delete()
            self.instance.delete()

        return self.instance
