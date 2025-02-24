import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quick.settings")
django.setup()

from rest_framework.test import APITestCase
from rest_framework import status
from apps.users.models import *
from apps.restaurants.models import *
from apps.menu.models import *
from apps.orders.models import *
from datetime import datetime


class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="adminuser", password="adminpass", email="admin@example.com"
        )
        self.restaurant = Restaurante.objects.create(name="Test Restaurant", address="123 Main St", rating=4.5, status="open", category="Fast Food", latitude=40.7128, longitude=-74.0060)
        self.menu_item = MenuItem.objects.create(name="Pizza", price=10.99, description="Delicious pizza", preparation_time=15, category="Fast Food", image_url="http://example.com/image.jpg", restaurant=self.restaurant)
        self.order = Order.objects.create(created_at=datetime(2024, 2, 1), status="pending", total_amount=20.99, delivery_address="123 Street", special_instructions="123 Street", estimated_delivery_time=datetime.now().isoformat(), customer=self.user, restaurant=self.restaurant)
        self.order_item = OrderItem.objects.create(created_at=datetime(2024, 2, 1), order=self.order, menu_item=self.menu_item, quantity=2, subtotal=21.98, notes="Extra cheese", active=True)
        response = self.client.post("/api/token/", {"username": "adminuser", "password": "adminpass"})
        self.token = response.data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

class UserAPITestCase(BaseAPITestCase):

    def test_get_users(self):
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        response = self.client.post(
            "/api/users/",
            {
                "username": "newuser", 
                "password": "securepass", 
                "email":"test@gmail.com",
                "first_name": "test",
                "last_name" : "test",
                "phone": "123456",
                "default_address" : "test",
                "typology": "dealer"
            },
            format="json"
        )
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
