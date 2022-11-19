from django.shortcuts import render, redirect
from django import forms

from photo_gallery.photos.forms import UploadPhotoForm
from photo_gallery.photos.models import BasePhotos


def UploadPhoto(request):
    photos = BasePhotos.objects.all()
    if request.method == 'GET':
        form = UploadPhotoForm()
    else:
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user profile', pk=request.user.pk)

    context = {
        'form': form,
        'photos': photos,
    }
    return render(request, 'photos/upload-photos.html', context)
