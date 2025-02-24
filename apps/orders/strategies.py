import csv
import json
from abc import ABC, abstractmethod
from decimal import Decimal

class ReportStrategy(ABC):
    @abstractmethod
    def generate(self, file_path, data):
        pass

class CSVReportStrategy(ReportStrategy):
    def generate(self, file_path, data):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['id', 'nombre', 'total_ventas', 'total_precio_ventas'])

            # Convertir objetos SalesReportDTO en listas
            writer.writerows([
                [row.restaurant_id, row.restaurant_name, row.total_sales, row.total_amount]
                for row in data
            ])

class JSONReportStrategy(ReportStrategy):
    def generate(self, file_path, data):
        with open(file_path, 'w') as file:
            json.dump([
                {
                    'id': row.restaurant_id,
                    'nombre': row.restaurant_name,
                    'total_ventas': row.total_sales,
                    'total_precio_ventas': str(row.total_amount)  # 🔹 Convertir Decimal a string
                }
                for row in data
            ], file, indent=4)