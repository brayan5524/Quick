import django_filters
from django import forms
from apps.users.models import User
from apps.restaurants.models import Restaurante

class UserFilter(django_filters.FilterSet):
    """Filtro avanzado para usuarios con widgets mejorados"""
    username = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    restaurant = django_filters.ModelChoiceFilter(
        queryset=Restaurante.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    phone = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
    )
    first_name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
    )
    last_name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
    )
    email = django_filters.CharFilter(
        lookup_expr='iexact',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}),
    )
    typology = django_filters.ChoiceFilter(
        choices=[('dealer', 'Dealer'), ('customer', 'Customer')],
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    created_at = django_filters.DateFilter(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    last_login = django_filters.DateFilter(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )

    class Meta:
        model = User
        fields = [
            'is_active', 'username', 'restaurant', 'first_name',
            'last_name', 'email', 'phone', 'typology', 'created_at', 'last_login'
        ]

