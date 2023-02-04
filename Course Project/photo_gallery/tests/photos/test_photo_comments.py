from django.test import TestCase
from django.urls import reverse_lazy

from photo_gallery.photos.models import PhotoComments
from tests.photos.test_photo_details import UserPhotosMixin


class PhotoCommentsTest(UserPhotosMixin,TestCase):
    @staticmethod
    def create_comment(user_pk, photo_id, comment):
        return PhotoComments.objects.create(user_id=user_pk, photo_id=photo_id,comment=comment)

    def setUp(self) -> None:
        self.logged_user = self.create_user(username='user1', password='user1pass')
        self.other_user = self.create_user(username='user2', password='user2pass')
        self.logged_user_photos = self.user_upload_astro_photos(self.logged_user, photos_number=1)
        self.other_user_photos = self.user_upload_astro_photos(self.other_user, photos_number=1)

        self.logged_user_comment = self.create_comment(user_pk=self.logged_user.pk,
                                                       photo_id=self.logged_user_photos[0].pk,
                                                       comment='This is a logged user`s comment!')
        self.other_user_comment = self.create_comment(user_pk=self.other_user.pk,
                                                       photo_id=self.other_user_photos[0].pk,
                                                       comment='This is a other user`s comment!')

    # Verifies that `edit comment` and `delete comment` are not available options for non logged user
    def test_non_logged_user_can_only_read_comments(self):
        photo_to_check = self.logged_user_photos[0]
        photo_data = self.client.get(reverse_lazy('details photo', kwargs={'slug': photo_to_check.slug}))
        self.assertFalse('edit comment' in str(photo_data.content))
        self.assertFalse('delete comment' in str(photo_data.content))

