from django.views import generic as views
from photo_gallery.photos.models import BasePhotos


class ItemsListView(views.ListView):
    template_name = 'index.html'
    model = BasePhotos
    paginate_by = 3


