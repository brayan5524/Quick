import csv
import os
from .repositories import *
from django.http import JsonResponse
from .strategies import *
class ReportService:

    strategies = {
        'csv': CSVReportStrategy(),
        'json': JSONReportStrategy()
    }

    @staticmethod
    def generate_sales_report(month, format='csv'):
        file_path = f'reports/sales_report_{month}.{format}'
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        
        
        if format not in ReportService.strategies:
            raise ValueError('Formato de reporte no soportado')
        
        data = ReportRepository.fetch_sales_report(month)
        if not data:
            return None
        
        ReportService.strategies[format].generate(file_path, data)
        
        return JsonResponse({"Reporte Generado con exito":file_path})