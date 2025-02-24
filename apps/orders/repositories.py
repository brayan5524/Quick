from django.db import connection
from .dtos import SalesReportDTO

class ReportRepository:
    @staticmethod
    def fetch_sales_report(month):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT r.id, r.name, COUNT(o.id) AS total_ventas, SUM(o.total_amount) AS total_precio_ventas
                FROM orders_order o
                JOIN restaurants_restaurante r ON o.restaurant_id = r.id
                WHERE EXTRACT(MONTH FROM o.created_at) = %s
                GROUP BY r.id, r.name
            """, [month])
            return [SalesReportDTO(*row) for row in cursor.fetchall()]