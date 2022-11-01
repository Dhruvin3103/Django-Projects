from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user(AbstractUser):
    mob_no = models.CharField(max_length=10,unique=True)
    imgs = models.ImageField(upload_to="image/")
    dob = models.DateField(null=True)

class Task(models.Model):
    title = models.CharField(max_length=200)
    user_fk = models.ForeignKey(user, on_delete=models.CASCADE,default='dc')
    def __str__(self):
        return self.title

class List(models.Model):
    # completed = 'c'
    # pending = 'p'
    status_choices = [
        (False,'pending'),
        (True,'completed'),
    ]
    title1 = models.CharField(max_length=200)
    status = models.BooleanField(default=False,choices=status_choices)
    desc = models.TextField(default='')
    start = models.DateTimeField(default='')
    end = models.DateTimeField(default='')
    task_FK = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.title1
