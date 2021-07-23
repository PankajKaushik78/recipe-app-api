from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        ''' Test whether user is created successfully with given email and password '''
        email = 'test@pankaj.com'
        password = 'Test123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized_email(self):
        ''' Checks whether new user email is normalized or not '''
        email = 'test@PANKAJ.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_invalid_user_email(self):
        ''' Check if user has provided valid email address or not '''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
            
    def test_create_new_superuser(self):
        ''' Tests creating a new superuser '''
        email = 'test@pankaj.com'
        password = 'Test123'
        user = get_user_model().objects.create_superuser(
            email = email,
            password = password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
