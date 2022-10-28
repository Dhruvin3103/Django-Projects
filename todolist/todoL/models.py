from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user(AbstractUser):
    mob_no = models.CharField(max_length=10,unique=True)
    img = models.ImageField(upload_to='todoL/images')
    dob = models.DateField(null=True)
class Task(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class List(models.Model):
    title1 = models.CharField(max_length=200)
    desc = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    task_FK = models.ForeignKey(Task, on_delete=models.CASCADE)