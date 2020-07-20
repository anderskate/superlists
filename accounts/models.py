import uuid

from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class ListUserManager(BaseUserManager):
    """List User manager"""

    def create_user(self, email):
        """Create User"""
        ListUser.objects.create(email=email)

    def create_superuser(self, email, password):
        """Create superuser"""
        self.create_user(email)


class Token(models.Model):
    """Marker"""
    email = models.EmailField()
    uid = models.CharField(default=uuid.uuid4, max_length=40)


class ListUser(AbstractBaseUser, PermissionsMixin):
    """List User"""
    email = models.EmailField(primary_key=True)
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email', 'height']

    objects = ListUserManager()

    @property
    def is_staff(self):
        return self.email == 'harry.percival@example.com'

    @property
    def is_active(self):
        return True


class User(models.Model):
    """User Model"""
    email = models.EmailField(primary_key=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True
