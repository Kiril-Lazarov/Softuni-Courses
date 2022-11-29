from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from photo_gallery.accounts.views import UserModel
from photo_gallery.photos.forms import AstroPhotographyAssessmentForm, PortraitPhotographyAssessmentForm, \
    StreetPhotographyAssessmentForm

from photo_gallery.photos.forms import UploadPhotoForm, EditPhotoForm, DeletePhotoForm, UploadAstroPhotoForm, \
    UploadStreetPhotoForm, UploadPortraitPhotoForm, AddCommentForm, EditCommentForm, DeleteCommentForm, photo_models
from photo_gallery.photos.models import BasePhotos, PhotoComments, PortraitPhotographyAssessment, \
    StreetPhotographyAssessment, AstroPhotographyAssessment


class PhotoCategoryFactory:
    category_form = {
        'astro_photography': UploadAstroPhotoForm,
        'portrait': UploadPortraitPhotoForm,
        'street': UploadStreetPhotoForm,
    }

    @classmethod
    def get_photo_category_form(cls, photo_category, request=None):
        return cls.category_form[photo_category](request)


def upload_photo_view(request):
    if request.method == 'GET':
        form = UploadPhotoForm()
    else:
        form = UploadPhotoForm(request.POST, request.FILES)
        photo = form.save(commit=False)
        photo_category = photo.category
        photo_category_form = PhotoCategoryFactory.get_photo_category_form(photo_category, request.POST)
        photo_assessment_model = photo_category_form.save(commit=False)
        if form.is_valid() and photo_category_form.is_valid():
            photo.user_id = request.user.pk
            photo.save()
            form.save_m2m()
            photo_assessment_model.user_id, photo_assessment_model.photo_id = request.user.pk, photo.pk
            photo_assessment_model.save()
            photo_category_form.save_m2m()
            return redirect('profile gallery', pk=request.user.pk)

    context = {
        'form': form,
    }
    return render(request, 'photos/upload-photos.html', context)


class PhotoDetailsView(views.DetailView):
    template_name = 'photos/photo-details.html'
    model = BasePhotos
    photo_assessments_models = photo_models

    def get_photo_slug(self):
        return list(self.request.get_full_path().split('/'))[-2]

    @staticmethod
    def get_model_field_names_and_values(assessment_model, photo_pk):
        excluded_fields = ('_state', 'id', 'photo_id', 'user_id', 'rating1')
        model_fields = {}
        curr_model = assessment_model.objects.filter(photo_id=photo_pk).get().__dict__
        for field, value in curr_model.items():
            if field not in excluded_fields:
                model_fields[field] = value
        return model_fields

    def get_success_url(self):
        return reverse_lazy('details photo', kwargs={
            'slug': self.get_photo_slug(),
        })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = self.model.objects.filter(slug=self.get_photo_slug()).get()
        context['photo'] = photo
        context['comments'] = PhotoComments.objects.filter(photo_id=photo.id).all()
        context['photo_assessments'] = \
            self.get_model_field_names_and_values(self.photo_assessments_models[photo.category], photo.pk)
        return context


# def photo_details_view(request, slug):
#     photo_assessments_models = {
#         'astro_photography': AstroPhotographyAssessment,
#         'portrait': PortraitPhotographyAssessment,
#         'street': StreetPhotographyAssessment,
#     }
#     photo = BasePhotos.objects.filter(slug=slug).get()
#     comments = PhotoComments.objects.filter(photo_id=photo.id).all()
#     photo_assessments = get_model_field_names_and_values(photo_assessments_models[photo.category], photo.pk)
#     print(photo_assessments)
#     # for assessment in photo_assessments:
#     #     print(assessment.name)
#     context = {
#         'photo': photo,
#         'comments': comments,
#         'photo_assessments': photo_assessments,
#     }
#     return render(request, 'photos/photo-details.html', context)

class ModelFormDispatcher:

    @staticmethod
    def get_form_assessment(category):
        assessment_model_forms = {
            'astro_photography': AstroPhotographyAssessmentForm,
            'portrait': PortraitPhotographyAssessmentForm,
            'street': StreetPhotographyAssessmentForm,
        }
        return assessment_model_forms[category]

    @staticmethod
    def get_model_assessment(category):
        photo_assessments_models = {
            'astro_photography': AstroPhotographyAssessment,
            'portrait': PortraitPhotographyAssessment,
            'street': StreetPhotographyAssessment,
        }
        return photo_assessments_models[category]


def photo_assessment_view(request, slug):
    dispatcher = ModelFormDispatcher
    photo = BasePhotos.objects.filter(slug=slug).get()
    assessment_form = dispatcher.get_form_assessment(photo.category)
    assessment_model = dispatcher.get_model_assessment(photo.category)
    assessment = assessment_model.objects.filter(photo_id=photo.pk, user_id=request.user.pk).get()
    if request.method == 'GET':
        form = assessment_form(instance=assessment)
    else:

        form = assessment_form(request.POST, instance=assessment)
        if form.is_valid():
            form.save()
            redirect('details photo', slug=photo.slug)

    context = {
        'form': form,
        'photo': photo,
    }
    return render(request, 'photos/assessment-photo.html', context)


def photo_edit_view(request, slug):
    photo = BasePhotos.objects.filter(slug=slug).get()
    if request.method == 'GET':
        form = EditPhotoForm(instance=photo)
    else:
        form = EditPhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('profile gallery', pk=request.user.pk)
    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, 'photos/photo-edit.html', context)


def delete_photo_view(request, slug):
    photo = BasePhotos.objects.filter(slug=slug).get()
    user = UserModel.objects.filter(pk=photo.user_id).get()
    if request.method == 'GET':
        form = DeletePhotoForm(instance=photo)
    else:
        form = DeletePhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('user profile', pk=user.pk)
    context = {
        'form': form,
        'user': user,
        'photo': photo,
    }

    return render(request, 'photos/photo-delete.html', context)


def add_photo_comment(request, pk, slug):
    photo = BasePhotos.objects.filter(slug=slug).get()
    form = AddCommentForm(request.POST)
    body = form.data['body']

    if form.is_valid():
        comment = form.save(commit=False)
        comment.photo_id = photo.id
        comment.user_id = pk
        comment.comment = body
        comment.save()

    return redirect('details photo', slug=photo.slug)


@login_required
def edit_photo_comment(request, pk):
    comment = PhotoComments.objects.filter(pk=pk).get()
    photo_id = comment.photo_id
    photo = BasePhotos.objects.filter(pk=photo_id).get()
    if request.method == "GET":
        form = EditCommentForm(instance=comment)
    else:
        form = EditCommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            return redirect('details photo', slug=photo.slug)
    context = {
        'form': form,
        'comment': comment,
        'photo': photo,
    }

    return render(request, 'comments/edit-comment.html', context)


def delete_photo_comment(request, pk, slug):
    photo = BasePhotos.objects.filter(slug=slug).get()
    if request.method == "GET":
        form = DeleteCommentForm()
    else:
        comment = PhotoComments.objects.filter(user_id=pk, photo_id=photo.pk).first()
        form = DeleteCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('details photo', slug=photo.slug)
    context = {
        'form': form,
        'photo': photo,
    }
    return render(request, 'comments/delete-comment.html', context)
