from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser, BaseModel, UserManager):
    """Model for user with no username field """
    username = None
    phone = models.CharField(_('phone number'), max_length=10, unique=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def _create_user(self, phone, password=None, **extra_fields):
        """Create and save a User with  phone number and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        self.phone=phone
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        """Create and save a SuperUser with phone number and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields )
