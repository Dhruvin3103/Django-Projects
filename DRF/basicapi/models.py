from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# Create your models here.
from .manager import UserManager

class User(AbstractUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    is_theatre_operator = models.BooleanField(default=False)
    is_movie_operator = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    mob = models.IntegerField(default=9000000000)
    age = models.IntegerField(default=17)


    objects = UserManager()

class theatreUser(models.Model):
    user = models.OneToOneField(User,default=1,on_delete=models.CASCADE)
