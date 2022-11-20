
from django.urls import path, include

from photo_gallery.photos.views import upload_photo_view, photo_details_view, photo_edit_view, delete_photo_view, \
    add_photo_comment, edit_photo_comment

urlpatterns = (
    path('upload/', upload_photo_view, name='upload photo'),
    path('details/<slug:slug>/', photo_details_view, name='details photo'),
    path('edit/<slug:slug>/', photo_edit_view, name='edit photo'),
    path('delete/<slug:slug>/', delete_photo_view, name='delete photo'),
    path('comment/', include([
        path('add/<int:pk>/<slug:slug>/', add_photo_comment, name='add photo comment'),
        path('edit/<int:pk>/<slug:slug>/', edit_photo_comment, name='edit photo comment'),
    ])),
)
