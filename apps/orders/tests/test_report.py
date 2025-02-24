import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quick.settings")
django.setup()

from rest_framework import status
from apps.users.tests.test_users import BaseAPITestCase

# Pruebas para reportes y carga de usuarios
class ReportsAPITestCase(BaseAPITestCase):
    def test_sales_report_flow(self):
        # Paso 1: Solicitar el reporte de ventas
        response = self.client.post("/api/reports/sales/2/", {"format": "csv"}, format="json")
        print("Step 1 - Request Report:", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Paso 2: Verificar el estado del reporte
        response = self.client.get("/api/reports/sales/status/2/")
        print("Step 2 - Check Report Status:", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Paso 3: Descargar el reporte
        response = self.client.get("/api/reports/sales/download/2/")
        csv_content = b"".join(response.streaming_content).decode("utf-8")
        print("Step 3 - Download Report:", csv_content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
