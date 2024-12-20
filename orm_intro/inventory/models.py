from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} {self.price} {self.stock}"