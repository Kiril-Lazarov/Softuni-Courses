from django.shortcuts import render, redirect

from photo_gallery.accounts.views import UserModel
from photo_gallery.photos.forms import UploadPhotoForm, EditPhotoForm, DeletePhotoForm, UploadAstroPhotoForm, \
    UploadStreetPhotoForm, UploadPortraitPhotoForm, AddCommentForm, EditCommentForm, DeleteCommentForm
from photo_gallery.photos.models import BasePhotos, PhotoComments


class PhotoCategoryFactory:
    category_form = {
        'astro_photography': UploadAstroPhotoForm,
        'portrait': UploadPortraitPhotoForm,
        'street': UploadStreetPhotoForm,
    }

    @classmethod
    def get_photo_category_form(cls, photo_category, request=None):
        return cls.category_form[photo_category](request)

    # @classmethod
    # def get_photo_category_model(cls, photo_category):


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
            photo_assessment_model.user_id = request.user.pk
            photo_assessment_model.photo_id = photo.pk
            photo_assessment_model.save()
            photo_category_form.save_m2m()
            return redirect('profile gallery', pk=request.user.pk)

    context = {
        'form': form,
    }
    return render(request, 'photos/upload-photos.html', context)


def photo_details_view(request, slug):
    photo = BasePhotos.objects.filter(slug=slug).get()
    comments = PhotoComments.objects.filter(photo_id=photo.id).all()

    context = {
        'photo': photo,
        'comments': comments,
    }
    return render(request, 'photos/photo-details.html', context)


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
