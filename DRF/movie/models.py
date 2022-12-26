from django.db import models

from theatre.models import theatre


# Create your models here.

class movie(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_time = models.DateTimeField()
    movie_lang = models.CharField(max_length=50)# lang includes english, hindi, anime ....
    movie_type = models.CharField(max_length=50)# type includes 2D,3D,imax ...
    movie_rating = models.IntegerField(default=17)# minimum age required to watch movie
    movie_hrs = models.IntegerField(default=2)# total watchtime of movie
    movie_ticket_price = models.IntegerField(default=100)
    no_of_seats = models.IntegerField(default=50)
    theatre_no = models.ForeignKey(theatre, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_name