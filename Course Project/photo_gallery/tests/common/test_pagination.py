import math

from django.test import TestCase
from django.urls import reverse_lazy

from photo_gallery.photos.models import BasePhotos
from tests.photos.test_photo_details import UserPhotosMixin


class PaginationTest(UserPhotosMixin, TestCase):
    @staticmethod
    def create_photos(user):
        for index in range(1, 11):
            return [BasePhotos.objects.create(title=f'Photo{i}',
                                              image='photos/photo',
                                              slug=f'Photo-{i}',
                                              category='astro_photography',
                                              user_id=user.pk) for i in range(1, 11)]

    def setUp(self) -> None:
        self.user = self.create_user(username='user1', password='user1pass')
        self.photos_list = self.create_photos(self.user)

    # Tests the number of pages 
    def test_index_pagination(self):
        response = self.client.get(reverse_lazy('index'))
        number_of_pages = response.context_data['paginator'].num_pages
        number_of_photos_per_page = response.context_data['paginator'].per_page
        expected_number_of_pages = math.ceil(len(self.photos_list) / number_of_photos_per_page)

        self.assertEqual(number_of_pages, expected_number_of_pages)

    # Tests the descending order of photo arrangement
    def test_published_dates(self):
        response = self.client.get(reverse_lazy('index'))
        data_list = list(response.context_data['object_list'])
        published_times = [data.__dict__['published_date'] for data in data_list]

        self.assertTrue(published_times[0] > published_times[1])
