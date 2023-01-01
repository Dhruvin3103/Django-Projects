from django.db import models
from movie.models import movie
from basicapi.models import User
from datetime import datetime
# Create your models here

class booking(models.Model):

    booking_time = models.DateTimeField(default=datetime.now())
    b_no_of_tickets = models.IntegerField(blank=False,default=1)
    movie_no = models.ForeignKey(movie,on_delete=models.CASCADE)
    booking_price = models.IntegerField(default=100)
    user_info = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

