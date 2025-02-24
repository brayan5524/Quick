"""
URL configuration for quick project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.orders.tasks import *
from apps.users.tasks import *

from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



schema_view = get_schema_view(
    openapi.Info(
        title="Restaurant API",
        default_version="v1",
        description="Documentación de la API para la gestión de pedidos y reportes",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="soporte@restaurantapi.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],  # 🔹 Se asegura de que Swagger no pida autenticación
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/menu/', include('apps.menu.api.urls')),
    path('api/orders/', include('apps.orders.api.urls')),
    path('api/restaurants/', include('apps.restaurants.api.urls')),
    path('api/users/', include('apps.users.api.urls')),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
    path('api/push_users/upload/', upload_users_view, name='upload_users'),
    path('api/reports/sales/<int:month>/', request_sales_report, name='request_sales_report'),
    path('api/reports/sales/status/<int:month>/', check_report_status, name='check_report_status'),
    path('api/reports/sales/download/<int:month>/', download_sales_report, name='download_sales_report'),



]


urlpatterns += [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)