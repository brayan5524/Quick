import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quick.settings")
django.setup()


from rest_framework import status
from apps.users.models import *
from apps.users.tests.test_users import BaseAPITestCase



class RestaurantAPITestCase(BaseAPITestCase):
    def test_get_restaurants(self):
        response = self.client.get("/api/restaurants/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_restaurant(self):

        response = self.client.post(
            "/api/restaurants/",
            {
                "name": "New Place",
                "address": "123 Food St",
                "rating": 4.7,
                "status": "open",
                "category": "Fast Food",
                "latitude": 40.7128,
                "longitude": -74.0060
            },
            format="json"  # 🔹 Esto asegura que se envíen como JSON
        )
        print("Response Data:", response.data)  # 🔹 Imprimir la respuesta de la API
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)