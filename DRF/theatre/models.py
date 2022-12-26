from django.db import models


# Create your models here.

class theatre(models.Model):
    theatre_name = models.CharField(max_length=100,default='The mall')
    theatre_add = models.TextField(max_length=1000,default='malad')
    theatre_loc = models.CharField(max_length=20, default='malad') # loactions so that it will easy to retrive dat
    no_of_halls = models.IntegerField(default=5)  # total no of theatre

    def __str__(self):
        return self.theatre_name