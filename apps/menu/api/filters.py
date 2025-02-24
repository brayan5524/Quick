import django_filters
from django import forms
from apps.restaurants.models import Restaurante
from apps.menu.models import MenuItem

class MenuItemFilter(django_filters.FilterSet):
    """Filtro para el modelo MenuItem con widgets mejorados"""

    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del platillo'}),
    )
    description = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
    )
    price = django_filters.NumberFilter(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio mínimo'}),
    )
    preparation_time = django_filters.NumberFilter(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tiempo de preparación máximo (minutos)'}),
    )
    category = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'}),
    )
    created_at = django_filters.DateTimeFilter(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    restaurant = django_filters.ModelChoiceFilter(
        queryset=Restaurante.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    class Meta:
        model = MenuItem
        fields = [
            'name', 'description', 'price', 'preparation_time', 'available',
            'category', 'active', 'created_at', 'restaurant'
        ]
