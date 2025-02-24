import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quick.settings")
django.setup()

from datetime import datetime
from rest_framework import status
from apps.users.models import *
from apps.users.tests.test_users import BaseAPITestCase



class OrderAPITestCase(BaseAPITestCase):
    def test_get_orders(self):
        response = self.client.get("/api/orders/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_order(self):
        response = self.client.post(
            "/api/orders/",
            {
                "status": "pending",
                "total_amount": 25.50,
                "delivery_address": "456 Avenue",
                "estimated_delivery_time": datetime.now().isoformat(),
                "customer": 1,
                "restaurant": 1
            },
            format="json"
        )
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)