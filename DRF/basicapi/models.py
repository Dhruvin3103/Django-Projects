from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .manager import UserManager

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    mob = models.IntegerField(validators=[MinLengthValidator(10),MaxLengthValidator(10)],default=0000000000)
    age = models.IntegerField(default=17)


    objects = UserManager()
class movie(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=00.00)

    @property
    def sale_price(self):
        return "%.2f"%(float(self.price)*0.8)

class article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title  