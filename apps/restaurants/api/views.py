from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.restaurants.models import *
from apps.restaurants.api.serializers import *
from rest_framework.pagination import PageNumberPagination
from apps.restaurants.api.filters import *

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all().prefetch_related('menuitem_set')
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RestaurantsFilter
    pagination_class = PageNumberPagination
