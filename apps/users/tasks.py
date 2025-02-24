# Carga masiva de usuarios desde CSV/XLSX
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
from .services import *
from .repositories import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



@swagger_auto_schema(
    method='post',
    operation_description="Carga masiva de usuarios desde un archivo CSV/XLSX, maximo 20 usuarios",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'file': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY)
        },
        required=['file']
    ),
    security=[],  # Elimina autenticación en Swagger
    responses={200: "Carga completada", 400: "Error en la carga"}
)



@api_view(['POST'])
@permission_classes([IsAdminUser])
def upload_users_view(request):
    if request.method == 'POST' and request.FILES.get('file'):
        try:
            file = request.FILES['file']
            file_name = default_storage.save(f'uploads/{file.name}', file)
            user_data = UserService.process_file(file.name)
            created_users = UserRepository.bulk_create_users(user_data)
            return JsonResponse({'message': 'Carga completada', 'users_created': created_users})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Debe enviar un archivo'}, status=400)