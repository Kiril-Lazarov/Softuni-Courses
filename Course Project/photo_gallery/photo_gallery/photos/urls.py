from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from photo_gallery.photos.views import UploadPhoto

urlpatterns = (
    path('upload/', UploadPhoto, name='upload photo'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,)
