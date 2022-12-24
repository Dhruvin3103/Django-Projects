from django.db import models


# Create your models here.

class theatre(models.Model):
    theatre_name = models.CharField(max_length=100)
    theatre_no = models.CharField(max_length=100,unique=True)
    theatre_add = models.TextField(max_length=1000)
    theatre_capacity = models.IntegerField(default=50)  # minimum age required to watch movie
    no_of_theatre = models.TimeField()  # total watchtime of movie

    def __str__(self):
        return self.theatre_name