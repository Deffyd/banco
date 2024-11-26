import django_filters
from .models import Cliente

class ClienteFilter(django_filters.FilterSet):
    activo = django_filters.BooleanFilter(field_name='activo', label='Activo')
    genero = django_filters.ChoiceFilter(field_name='genero', choices=Cliente.GENERO_CHOICES, label='Género')
    nivel_de_satisfaccion = django_filters.NumberFilter(field_name='nivel_de_satisfaccion', label='Nivel de Satisfacción')
    nivel_de_satisfaccion_gte = django_filters.NumberFilter(field_name='nivel_de_satisfaccion', lookup_expr='gte', label='Nivel de Satisfacción Mayor o Igual a')
    nivel_de_satisfaccion_lte = django_filters.NumberFilter(field_name='nivel_de_satisfaccion', lookup_expr='lte', label='Nivel de Satisfacción Menor o Igual a')

    class Meta:
        model = Cliente
        fields = ['activo', 'genero', 'nivel_de_satisfaccion']
