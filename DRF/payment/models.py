from datetime import datetime
from booking.models import booking
from django.db import models

# Create your models here.

class payment(models.Model):

    p_upi_id = models.CharField(max_length=30)
    p_booking_id = models.ForeignKey(booking,on_delete=models.CASCADE,default=21)
    p_time = models.DateTimeField(default=datetime.now())
    p_price = models.IntegerField(default=100)
    p_done = models.BooleanField(default=False)

    def __str__(self):
        return self.p_upi_id
