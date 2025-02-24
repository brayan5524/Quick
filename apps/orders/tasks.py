import os
from django.http import FileResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes

from .services import *


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

def get_report_path(month, format):
    return f'reports/sales_report_{month}.{format}'  # Ruta absoluta dentro del contenedor





@swagger_auto_schema(
    method='post',
    operation_description="Generar reporte de ventas por mes",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'format': openapi.Schema(type=openapi.TYPE_STRING, enum=['csv', 'json'])
        }
    ),
    security=[],  # No requiere autenticación en Swagger
    manual_parameters=[],
    responses={200: "Reporte en proceso", 400: "Error al generar reporte"}
)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def request_sales_report(request, month):
    format = request.data.get('format', 'csv').strip().lower() 
    return ReportService.generate_sales_report(month, format)




@swagger_auto_schema(
    method='get',
    operation_description="Verificar estado del reporte",
    manual_parameters=[
        openapi.Parameter('format', openapi.IN_QUERY, description="Formato del reporte", type=openapi.TYPE_STRING, enum=['csv', 'json']),
    ],
    security=[],
    responses={200: "Estado del reporte", 404: "Reporte no encontrado"}
)
@api_view(['GET'])
@permission_classes([IsAdminUser])
def check_report_status(request, month):
    format = request.GET.get('format', 'csv').strip().lower() 
    print("uuu: ",format)
    file_path = get_report_path(month, format)
    if os.path.exists(file_path):
        return JsonResponse({'status': 'ready', 'download_url': f'/api/reports/sales/download/{month}/'})
    return JsonResponse({'status': 'processing'})



@swagger_auto_schema(
    method='get',
    operation_description="Descargar reporte generado",
    manual_parameters=[
        openapi.Parameter('format', openapi.IN_QUERY, description="Formato del reporte", type=openapi.TYPE_STRING, enum=['csv', 'json']),
    ],
    security=[],
    responses={200: "Archivo de reporte", 404: "Archivo no encontrado"}
)
@api_view(['GET'])
@permission_classes([IsAdminUser])
def download_sales_report(request, month):
    format = request.GET.get('format', 'csv').strip().lower() 
    file_path = get_report_path(month, format)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=f"sales_report_{month}.csv")
        os.remove(file_path)  # Eliminar después de la descarga
        return response
    return JsonResponse({'error': 'Archivo no encontrado'}, status=404)