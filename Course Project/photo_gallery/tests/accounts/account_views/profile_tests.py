from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from photo_gallery.accounts.models import Gender

UserModel = get_user_model()


class ProfileModelTests(TestCase):
    # Tests chars_validator when user inputs first (or last) name which contains one non letter char, expected
    # to raise ValidationError
    def test_chars_validator_with_non_letter_char(self):
        username = "Koko"
        email = 'koko@abv.bg'
        gender = Gender.choices()[0][0]
        password = 'qwert'

        user = UserModel(
            username=username,
            email=email,
            password=password,
            gender=gender,
        )

        first_name_of_user = 'Kokoko1'
        user.first_name = first_name_of_user

        with self.assertRaises(ValidationError) as er:
            user.full_clean()
            user.save()
            self.assertEqual('Name must content only letters.', str(er.exception))
            self.assertEqual(user.first_name, first_name_of_user)

    # Tests char_validator with correct input
    def test_chars_validator_with_correct_chars(self):
        username = "Koko"
        email = 'koko@abv.bg'
        gender = Gender.choices()[0][0]
        password = 'qwert'

        user = UserModel(
            username=username,
            email=email,
            password=password,
            gender=gender,
        )

        first_name_of_user = 'Kokoko'
        user.first_name = first_name_of_user

        user.full_clean()
        user.save()

        self.assertEqual(user.first_name, first_name_of_user)
