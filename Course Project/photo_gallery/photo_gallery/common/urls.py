from django.urls import path

from photo_gallery.common.views import index

urlpatterns = (
    path('', index, name='index'),
)