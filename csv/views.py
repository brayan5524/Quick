
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, FileResponse
from .tasks import generate_csv_report_task
from django.core.files.storage import default_storage

@api_view(['GET'])
def generate_report(request):
    task = generate_csv_report_task.delay()
    return JsonResponse({'task_id': task.id, 'message': 'Generación del reporte en proceso'})

@api_view(['GET'])
def download_report(request):
    file_path = 'reports/orders_report.csv'
    if default_storage.exists(file_path):
        return FileResponse(default_storage.open(file_path, 'rb'), as_attachment=True, filename="orders_report.csv")
    return JsonResponse({'error': 'Archivo no encontrado'}, status=404)