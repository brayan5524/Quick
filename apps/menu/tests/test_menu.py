import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quick.settings")
django.setup()



from rest_framework import status
from apps.users.models import *
from apps.users.tests.test_users import BaseAPITestCase
from apps.menu.models import *

class MenuAPITestCase(BaseAPITestCase):

    def test_get_menu_items(self):
        response = self.client.get("/api/menu/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_create_menu_item(self):
        response = self.client.post(
            "/api/menu/",
            {
                "name": "Burger",
                "description": "Tasty burger",
                "price": 8.99,
                "preparation_time": 10,
                "category": "Fast Food",
                "image_url": "http://example.com/burger.jpg",
                "restaurant": 1  # ID de restaurante válido
            },
            format="json"  # 🔹 Esto asegura que se envíen como JSON
        )
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)