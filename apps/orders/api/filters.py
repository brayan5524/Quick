import django_filters
from django import forms
from apps.orders.models import Order, OrderItem
from apps.users.models import User
from apps.restaurants.models import Restaurante
from apps.menu.models import MenuItem

class OrderFilter(django_filters.FilterSet):
    """Filtro para el modelo Order"""

    customer = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Cliente'
    )
    restaurant = django_filters.ModelChoiceFilter(
        queryset=Restaurante.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Restaurante'
    )
    status = django_filters.CharFilter(
        lookup_expr='icontains',  # Filtra por estado (insensible a mayúsculas/minúsculas)
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
        label='Estado'
    )
    total_amount = django_filters.NumberFilter(
        lookup_expr='gte',  # Filtra por monto total mayor o igual a un valor
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto total mínimo'}),
        label='Monto total'
    )
    created_at = django_filters.DateTimeFilter(
        lookup_expr='gte',  # Filtra por fecha de creación mayor o igual a una fecha
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Fecha de creación'
    )
    updated_at = django_filters.DateTimeFilter(
        lookup_expr='gte',  # Filtra por fecha de actualización mayor o igual a una fecha
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Fecha de actualización'
    )

    class Meta:
        model = Order
        fields = [
            'customer', 'restaurant', 'status', 'total_amount', 'active', 'created_at', 'updated_at'
        ]


class OrderItemFilter(django_filters.FilterSet):
    """Filtro para el modelo OrderItem"""

    order = django_filters.ModelChoiceFilter(
        queryset=Order.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Orden'
    )
    menu_item = django_filters.ModelChoiceFilter(
        queryset=MenuItem.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Ítem del Menú'
    )
    quantity = django_filters.NumberFilter(
        lookup_expr='gte',  # Filtra por cantidad mayor o igual a un valor
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad mínima'}),
        label='Cantidad'
    )
    subtotal = django_filters.NumberFilter(
        lookup_expr='gte',  # Filtra por subtotal mayor o igual a un valor
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Subtotal mínimo'}),
        label='Subtotal'
    )
    created_at = django_filters.DateTimeFilter(
        lookup_expr='gte',  # Filtra por fecha de creación mayor o igual a una fecha
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Fecha de creación'
    )
    updated_at = django_filters.DateTimeFilter(
        lookup_expr='gte',  # Filtra por fecha de actualización mayor o igual a una fecha
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Fecha de actualización'
    )

    class Meta:
        model = OrderItem
        fields = [
            'order', 'menu_item', 'quantity', 'subtotal', 'active', 'created_at', 'updated_at'
        ]