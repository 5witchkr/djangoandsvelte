from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True)
    nickname = models.CharField(max_length=24, unique=True)

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table= "User"