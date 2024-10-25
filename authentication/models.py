import typing

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.backends import ModelBackend

from django.db import models

class UserManager(BaseUserManager):
    def create_user(self,  email,password, first_name, last_name, date_of_birth, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save()
        return user

    def create_customer(self,  email,password, first_name, last_name, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,  email, password, first_name, last_name, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class User(AbstractUser):

    id = models.IntegerField(primary_key=True, auto_created= True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, unique=True, null=True)
    password = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    profile_picture = models.ImageField(upload_to='images/user_profile', null=True)

    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']

    objects = UserManager()

    def __str__(self):
        return self.email

    objects = UserManager()

# class CustomBackend(ModelBackend):
#     def authenticate(self, email=None, password=None, **kwargs) -> typing.Optional[BaseUser]:
#          try:
#              user = BaseUser.objects.get(email=email)
#              if user.check_password(password):
#                  return user
#
#          except BaseUser.DoesNotExist:
#              return None
#
#     def get_user(self, user_id, **kwargs) -> typing.Optional[BaseUser]:
#         try:
#             return BaseUser.objects.get(pk=user_id)
#         except BaseUser.DoesNotExist:
#             return None
