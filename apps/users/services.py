import pandas as pd
from django.core.files.storage import default_storage
from celery import shared_task
import os
from .strategies import *
from .dtos import UserDTO

def get_upload_path(file_name):
    return os.path.join('/quick/uploads', file_name)
    
class UserService:

    strategies = {
        '.csv': CSVStrategy(),
        '.xls': ExcelStrategy(),
        '.xlsx': ExcelStrategy()
    }

    @staticmethod
    def process_file(file_path):
        print("tttt: ",file_path)
        file_path = get_upload_path(file_path)


        if not os.path.exists(file_path):
            return {'error': 'El archivo no existe'}
    
        _, file_extension = os.path.splitext(file_path)

        if file_extension not in UserService.strategies:
            raise ValueError('Formato de archivo no permitido')
        
        data = UserService.strategies[file_extension].process(file_path)
        
        if len(data) > 20:
            raise ValueError('Solo se permite cargar hasta 20 usuarios a la vez')
        
        return [UserDTO(**row) for row in data]
    