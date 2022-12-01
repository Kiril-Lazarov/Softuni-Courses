from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from photo_gallery.accounts.views import UserModel
from photo_gallery.photos.forms import AstroPhotographyAssessmentForm, PortraitPhotographyAssessmentForm, \
    StreetPhotographyAssessmentForm

from photo_gallery.photos.forms import UploadPhotoForm, EditPhotoForm, DeletePhotoForm, AddCommentForm, EditCommentForm, \
    DeleteCommentForm, photo_models
from photo_gallery.photos.models import BasePhotos, PhotoComments


@login_required
def upload_photo_view(request):
    if request.method == 'GET':
        form = UploadPhotoForm()
    else:
        form = UploadPhotoForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.user_id = request.user.pk
            photo.save()
            form.save_m2m()
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
    def get_model_field_names_and_values(assessment_model, photo):
        excluded_fields = ('_state', 'id', 'photo_id', 'owner_id', 'rating1', 'assessing_user')
        model_fields = {}
        photo_assessments = list(assessment_model.objects.values().all())

        for assessment_pairs in photo_assessments:
            for field, value in assessment_pairs.items():
                if field not in excluded_fields:
                    if field not in model_fields:
                        model_fields[field] = value
                    else:
                        model_fields[field] += value
        return model_fields

    def get_success_url(self):
        return reverse_lazy('details photo', kwargs={
            'slug': self.get_photo_slug(),
        })

    def photo_user_rating_status(self, photo):
        assessing_users_list = list(self.photo_assessments_models[photo.category].
                                    objects.values_list('assessing_user', flat=True))
        return 'Rate' if self.request.user.pk not in assessing_users_list else 'Edit rate'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = self.model.objects.filter(slug=self.get_photo_slug()).get()
        context['photo'] = photo
        context['comments'] = PhotoComments.objects.filter(photo_id=photo.id).all()
        context['photo_assessments'] = \
            self.get_model_field_names_and_values \
                (self.photo_assessments_models[photo.category], photo)
        context['is_rated_from_user'] = self.photo_user_rating_status(photo)
        return context


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
        photo_assessments_models = photo_models
        return photo_assessments_models[category]


def photo_assessment_view(request, slug):
    dispatcher = ModelFormDispatcher
    photo = BasePhotos.objects.filter(slug=slug).get()
    assessment_form = dispatcher.get_form_assessment(photo.category)
    assessment_model = dispatcher.get_model_assessment(photo.category)

    try:
        assessment = assessment_model.objects.filter(assessing_user=request.user.pk).get()
    except ObjectDoesNotExist as ex:
        assessment_model.objects.create(photo_id=photo.pk, owner_id=photo.user_id, assessing_user=request.user.pk)
        assessment = assessment_model.objects.filter(assessing_user=request.user.pk).get()

    if request.method == 'GET':
        form = assessment_form(instance=assessment)
    else:
        form = assessment_form(request.POST, instance=assessment)
        if form.is_valid():
            pre_save_form = form.save(commit=False)
            pre_save_form.assessing_user = request.user.pk
            pre_save_form.save()
            return redirect('details photo', slug=photo.slug)

    context = {
        'form': form,
        'photo': photo,
    }
    return render(request, 'photos/assessment-photo.html', context)


@login_required
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


@login_required
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


@login_required
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
