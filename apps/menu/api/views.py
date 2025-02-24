from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.menu.models import *
from apps.menu.api.serializers import *
from rest_framework.pagination import PageNumberPagination
from apps.menu.api.filters import *

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().select_related('restaurant')
    serializer_class = MenuItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MenuItemFilter
    pagination_class = PageNumberPagination
    


