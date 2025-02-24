from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.orders.models import *
from apps.orders.api.serializers import *
from rest_framework.pagination import PageNumberPagination
from apps.orders.api.filters import *


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().select_related('restaurant', 'customer').prefetch_related('orderitem_set')
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter
    pagination_class = PageNumberPagination



class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all().select_related('order', 'menu_item')
    serializer_class = OrderItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderItemFilter
    pagination_class = PageNumberPagination
