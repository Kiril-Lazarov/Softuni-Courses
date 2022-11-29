
from django.urls import path, include

# from photo_gallery.photos.assesssments_form import SelectPhotoModelForm
from photo_gallery.photos.views import upload_photo_view, PhotoDetailsView, photo_edit_view, delete_photo_view, \
    add_photo_comment, delete_photo_comment, edit_photo_comment, photo_assessment_view

urlpatterns = (
    path('upload/', upload_photo_view, name='upload photo'),
    path('details/<slug:slug>/', PhotoDetailsView.as_view(), name='details photo'),
    path('details/assessment/<slug:slug>/', photo_assessment_view,name='photo assessment'),
    path('edit/<slug:slug>/', photo_edit_view, name='edit photo'),
    path('delete/<slug:slug>/', delete_photo_view, name='delete photo'),
    path('comment/', include([
        path('add/<int:pk>/<slug:slug>/', add_photo_comment, name='add photo comment'),
        path('edit/<int:pk>/', edit_photo_comment, name='edit photo comment'),
        path('delete/<int:pk>/<slug:slug>/', delete_photo_comment, name='delete photo comment'),
    ])),
)
