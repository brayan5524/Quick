from django.db import models
from apps.restaurants.models import Restaurante
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    restaurant = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    default_address = models.TextField()
    typology = models.CharField(max_length=20, choices=[('dealer', 'Dealer'), ('customer', 'Customer')])
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"