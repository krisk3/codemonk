"""
Defines database models for the Django application.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    """
    Manager for users.

    Provides methods for creating and managing user instances.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create, save and return a new user.

        Parameters:
        - email (str): Email address for the user.
        - password (str): Password for the user.
        - extra_fields (dict): Additional fields for the user.

        Raises:
        - ValueError: If email is not provided.

        Returns:
        - User: Newly created user instance.
        """
        if not email:
            raise ValueError("User must have an email address.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and return a new superuser.

        Parameters:
        - email (str): Email address for the superuser.
        - password (str): Password for the superuser.

        Returns:
        - User: Newly created superuser instance.
        """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User in the system.

    Represents a user with email as the unique identifier.
    """

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        """
        Return a string representation of the user.

        Returns:
        - str: Email address of the user.
        """
        return self.email
