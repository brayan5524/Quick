from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quick.settings')

app = Celery('quick')

# Cargar configuración desde Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descubrir tareas automáticamente en todas las aplicaciones instaladas
from django.conf import settings
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
