from rest_framework import serializers
from apps.restaurants.models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'