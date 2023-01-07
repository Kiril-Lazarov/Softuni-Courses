from django.core.exceptions import ValidationError
from django.test import TestCase

from photo_gallery.accounts.models import AppUser
from photo_gallery.accounts.views import UserEditView


class ProfileModelTests(TestCase):
    #Tests chars_validator when user inputs first (or last) name which contains only letters
    def test_chars_validator(self):
        profile = AppUser(
            username='Koko',
            email='koko@abv.bg',
            password='qwert',
            gender='Do not show',
        )

        first_name_of_user = 'Kokoko1'
        profile.first_name = first_name_of_user

        with self.assertRaises(ValidationError) as er:
            profile.save()
            self.assertEqual('Name must content only letters.', str(er.exception))
        # self.assertEqual(profile.first_name, first_name_of_user)
