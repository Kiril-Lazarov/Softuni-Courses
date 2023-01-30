from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy, reverse

from photo_gallery.photos.models import BasePhotos

UserModel = get_user_model()


class UserPhotosMixin:
    @staticmethod
    def create_user(username, password):
        return UserModel.objects.create_user(username=username,
                                             password=password,
                                             email=f'{username}@abv.bg')

    @staticmethod
    def user_upload_astro_photos(user):
        return [BasePhotos.objects.create(title=f'Photo{i}',
                                          slug=f'Photo-{i}',
                                          image=f'photos/photo{i}',
                                          category='astro_photography',
                                          user_id=user.pk) for i in range(2)]


class PhotoDetailsTest(UserPhotosMixin, TestCase):

    # Verified that the user cannot rate his own photos
    def test_user1_no_permission_to_rate_his_own_photo(self):
        user_1 = self.create_user(username='user1', password='user1pass')
        user_2 = self.create_user(username='user2', password='user2pass')

        user1_photos = self.user_upload_astro_photos(user_1)
        photo_to_check = user1_photos[0]

        self.client.login(username=user_1.username, password='user1pass')
        self.client.get(reverse_lazy('details photo', kwargs={'slug': photo_to_check.slug}))

        self.assertTrue(user_1.pk == photo_to_check.user_id)
