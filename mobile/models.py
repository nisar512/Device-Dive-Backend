from django.db import models

# Create your models here.
class Mobile(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/',null=True)
    def __str__(self):
        return f"{self.brand} {self.name}"
