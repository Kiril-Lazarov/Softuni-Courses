from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from photo_gallery.photos.models import BasePhotos, AstroPhotographyAssessment

UserModel = get_user_model()


class UserPhotosMixin:
    @staticmethod
    def create_user(username, password):
        return UserModel.objects.create_user(username=username,
                                             password=password,
                                             email=f'{username}@abv.bg')

    @staticmethod
    def user_upload_astro_photos(user, photos_number):
        return [BasePhotos.objects.create(title=f'Photo{i}',
                                          slug=f'Photo-{i}',
                                          image=f'photos/photo{i}',
                                          category='astro_photography',
                                          user_id=user.pk) for i in range(photos_number)]


class PhotoDetailsTest(UserPhotosMixin, TestCase):
    def setUp(self) -> None:
        self.logged_user = self.create_user(username='user1', password='user1pass')
        self.other_user = self.create_user(username='user2', password='user2pass')
        self.logged_user_photos = self.user_upload_astro_photos(self.logged_user, photos_number=1)
        self.other_user_photos = self.user_upload_astro_photos(self.other_user, photos_number=1)

    # Verifies that the user cannot rate his own photo
    def test_logged_user_no_permission_to_rate_his_own_photo(self):
        photo_to_check = self.logged_user_photos[0]
        self.client.login(username=self.logged_user.username, password='user1pass')
        self.client.get(reverse_lazy('details photo', kwargs={'slug': photo_to_check.slug}))
        self.assertEqual(self.logged_user.pk, photo_to_check.user_id)

    # Verifies that the user can rate other user photo when the photo is not yet rated by him
    def test_logged_user_permission_to_rate_other_user_photos(self):
        photo_to_check = self.other_user_photos[0]
        self.client.login(username=self.logged_user.username, password='user1pass')
        response = self.client.get(reverse_lazy('details photo', kwargs={'slug': photo_to_check.slug}))
        self.assertNotEqual(self.logged_user.pk, photo_to_check.user_id)
        self.assertEqual(response.context_data['is_rated_from_user'], 'Rate')

    # Verifies that initial logged user assessments values for the photo are equal to zero
    def test_initial_assessments_values(self):
        photo_to_check = self.other_user_photos[0]
        self.client.login(username=self.logged_user.username, password='user1pass')
        response = self.client.get(reverse_lazy('photo assessment', kwargs={'slug': photo_to_check.slug}))
        assessment_values_list = []

        # Take needed assessment values from response.context and append them to list
        for i in range(17, 39, 5):
            assessment_values_list.append(int(response.context[i]["widget"]["value"]))
        self.assertEqual(sum(assessment_values_list), 0)

    # Verifies that the user can rate other user photo when the photo is already rated by him
    def test_logged_user_already_rate_other_user_photo(self):
        photo_to_check = self.logged_user_photos[0]
        AstroPhotographyAssessment.objects.create(
            photo_id=photo_to_check.pk,
            owner_id=self.other_user.pk,
            rating1=0,
            contrast=1,
            detail=2,
            focus=3,
            light=4,
            color_temperature=2,
            assessing_user=self.logged_user.pk,
        )
        self.client.login(username=self.logged_user.username, password='user1pass')
        assessed_photo = AstroPhotographyAssessment.objects.filter(
            assessing_user=self.logged_user.pk, photo_id=photo_to_check.pk).get()

        response = self.client.get(reverse_lazy('details photo', kwargs={'slug': photo_to_check.slug}))

        self.assertEqual(self.logged_user.pk, assessed_photo.assessing_user)
        self.assertEqual(response.context_data['is_rated_from_user'], 'Edit rate')

    # Verifies correct assessments values already given by logged user for particular photo
    def test_assessments_values_for_editing(self):
        photo_to_check = self.logged_user_photos[0]
        AstroPhotographyAssessment.objects.create(
            photo_id=photo_to_check.pk,
            owner_id=self.other_user.pk,
            rating1=0,
            contrast=6,
            detail=3,
            focus=2,
            light=2,
            color_temperature=6,
            assessing_user=self.logged_user.pk,
        )

        logged_user_assessments_items = {
            'light': 2,
            'focus': 2,
            'detail': 3,
            'contrast': 6,
            'color_temperature': 6,
        }
        self.client.login(username=self.logged_user.username, password='user1pass')

        response = self.client.get(reverse_lazy('photo assessment', kwargs={'slug': photo_to_check.slug}))
        response_context_items = {}
        for i in range(17, 39, 5):
            response_context_items[response.context[i]["widget"]["name"]] = int(response.context[i]["widget"]["value"])
        self.assertEqual(logged_user_assessments_items, response_context_items)
