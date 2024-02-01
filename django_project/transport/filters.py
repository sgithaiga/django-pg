import django_filters
from .models import Fuel_mgt
from django_filters import CharFilter


class RequestFilter(django_filters.FilterSet):
    #region = django_filters.CharFilter(field_name="region")
    registration_no = django_filters.CharFilter(field_name="registration_no")
    fuel_type_requested = django_filters.CharFilter(field_name="fuel_type_requested")
    
    class Meta:
        model = Fuel_mgt
        fields = ['region', 'registration_no',  'fuel_type_requested',]