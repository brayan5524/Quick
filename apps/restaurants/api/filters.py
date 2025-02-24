import django_filters
from django import forms
from apps.users.models import User
from apps.restaurants.models import Restaurante

class RestaurantsFilter(django_filters.FilterSet):
    """Filtro avanzado para usuarios con widgets mejorados"""
    name = django_filters.CharFilter(
        lookup_expr='icontains',  # Filtra por nombre (de forma insensible a mayúsculas/minúsculas)
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Restaurante'})
    )
    address = django_filters.CharFilter(
        lookup_expr='icontains',  # Filtra por dirección (insensible a mayúsculas/minúsculas)
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'})
    )
    rating = django_filters.NumberFilter(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Calificación mínima'})
    )
    category = django_filters.CharFilter(
        lookup_expr='icontains',  # Filtra por categoría (insensible a mayúsculas/minúsculas)
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categoría'})
    )
    status = django_filters.ChoiceFilter(
        choices=[('open', 'Abierto'), ('closed', 'Cerrado')],  # Filtra por estado del restaurante
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    created_at = django_filters.DateTimeFilter(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    updated_at = django_filters.DateTimeFilter(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    class Meta:
        model = Restaurante
        fields = [
            'name', 'address', 'rating', 'category', 'status', 'active', 'created_at', 'updated_at'
        ]



