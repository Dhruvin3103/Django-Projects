from django.db import models

# Create your models here.
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