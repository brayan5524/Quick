from django.db import models
from apps.restaurants.models import Restaurante
# Create your models here.
class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.IntegerField()
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name