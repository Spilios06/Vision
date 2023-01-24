from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'email'