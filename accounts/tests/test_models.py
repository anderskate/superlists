from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Token

User = get_user_model()

class UserModelTest(TestCase):
    """Test User Model"""

    def test_user_is_valid_with_email_only(self):
        """User only required email"""
        user = User(email='a@b.com')
        user.full_clean()

    def test_email_is_primary_key(self):
        """Test: Email address is primary key"""
        user = User(email='a@b.com')
        self.assertEqual(user.pk, 'a@b.com')

    def test_links_user_with_auto_generated_uid(self):
        """Test: Connecting user with auto generic uid"""
        token1 = Token.objects.create(email='a@b.com')
        token2 = Token.objects.create(email='a@b.com')
        self.assertNotEqual(token1.uid, token2.uid)
