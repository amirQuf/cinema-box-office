from django.db import models


from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    mobile = models.CharField(max_length=11)
