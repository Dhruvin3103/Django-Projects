from datetime import datetime

from django.db import models

# Create your models here.

class payment(models.Model):
    p_choices=(
        (1,'Gpay'),
        (2,'paytm'),
        (3,'upi')
    )
    payment_method = models.CharField(max_length=20,choices=p_choices)
    p_upi_id = models.CharField(max_length=30)
    p_time = models.DateTimeField(default=datetime.now())
    p_price = models.IntegerField()

    def __str__(self):
        return self.p_upi_id
