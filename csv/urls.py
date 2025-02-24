from django.urls import path
from .views import generate_report, download_report

urlpatterns = [
    path('generate_report/', generate_report, name='generate_report'),
    path('download_report/', download_report, name='download_report'),
]
