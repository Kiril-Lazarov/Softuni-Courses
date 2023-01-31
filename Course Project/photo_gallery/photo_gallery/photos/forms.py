from django import forms
from django.contrib.auth import get_user_model

from photo_gallery.photos.models import BasePhotos, AstroPhotographyAssessment, PortraitPhotographyAssessment, \
    StreetPhotographyAssessment, PhotoComments

photo_models = {
    'astro_photography': AstroPhotographyAssessment,
    'portrait': PortraitPhotographyAssessment,
    'street': StreetPhotographyAssessment,
}

UserModel = get_user_model()


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


class UploadStreetPhotoForm(forms.ModelForm):
    class Meta:
        model = StreetPhotographyAssessment
        fields = ('rating1',)

    @classmethod
    def get_model(cls):
        if __name__ == '__main__':
            return StreetPhotographyAssessment


class UploadPortraitPhotoForm(forms.ModelForm):
    class Meta:
        model = PortraitPhotographyAssessment
        fields = ('rating1',)

    @classmethod
    def get_model(cls):
        if __name__ == '__main__':
            return PortraitPhotographyAssessment


class EditPhotoForm(forms.ModelForm):
    class Meta:
        model = BasePhotos
        exclude = ('slug', 'image', 'user', 'category')


class DeletePhotoForm(forms.ModelForm):
    class Meta:
        model = BasePhotos
        exclude = ('title', 'image', 'description', 'slug', 'user', 'published_date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].required = False

    def save(self, commit=True):
        if commit:
            photo_id = self.instance.pk
            photo = BasePhotos.objects.filter(pk=photo_id).get()
            photo_assessment = photo_models[photo.category].objects.all()
          
            if photo_assessment:
                for assessment in photo_assessment:
                    if assessment.photo_id == photo_id:
                        assessment.delete()
            self.instance.delete()
        return self.instance
    # TODO: Delete the images from media_files
    # def delete_image_from_media_files(self, image=None):
    #         # You have to prepare what you need before delete the model
    #         storage, path = self.image.storage, self.image.path
    #         # Delete the model before the file
    #         super(Profile, self).delete(*args, **kwargs)
    #         # Delete the file after the model
    #         storage.delete(path)
    #
    #     return self.instance


class BaseCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComments
        fields = ('comment',)


class AddCommentForm(BaseCommentForm):
    pass


class EditCommentForm(BaseCommentForm):
    pass


class DeleteCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComments
        exclude = ('user', 'photo', 'comment', 'published_date',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class AstroPhotographyAssessmentForm(forms.ModelForm):
    class Meta:
        model = AstroPhotographyAssessment
        exclude = ('_state', 'id', 'photo_id', 'owner', 'rating1', 'photo', 'user', 'assessing_user')


class PortraitPhotographyAssessmentForm(forms.ModelForm):
    class Meta:
        model = PortraitPhotographyAssessment
        exclude = ('_state', 'id', 'photo_id', 'owner', 'rating1', 'photo', 'user', 'assessing_user')


class StreetPhotographyAssessmentForm(forms.ModelForm):
    class Meta:
        model = StreetPhotographyAssessment
        exclude = ('_state', 'id', 'photo_id', 'owner', 'rating1', 'photo', 'user', 'assessing_user')


