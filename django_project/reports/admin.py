import datetime
from django import forms
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields, widgets
from django.utils import timezone
from .models import Historic_Consumption

class NaiveDateWidget(widgets.DateTimeWidget):
    def clean(self, value, row=None, *args, **kwargs):
        # Parse string values as datetime objects
        if isinstance(value, str):
            # Parse the string to a datetime object
            value = timezone.make_aware(datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S'), timezone=timezone.utc)
            # Remove the time part, leaving only the date
            value = timezone.make_aware(datetime.datetime(value.year, value.month, value.day), timezone=timezone.utc)

        # Check if the value is aware and make it naive
        if timezone.is_naive(value):
            value = timezone.localtime(timezone.make_aware(value, timezone=timezone.utc))

        return value

    def render(self, value, obj=None):
        # Format the date as 'YYYY-MM-DD'
        if value:
            return value.strftime('%Y-%m-%d')
        return super().render(value, obj)

class HistoricConsumptionResource(resources.ModelResource):
    consumption_date = fields.Field(
        column_name='consumption_date',
        attribute='consumption_date',
        widget=NaiveDateWidget(format='%Y-%m-%d %H:%M:%S'),
    )

    class Meta:
        model = Historic_Consumption
        exclude = ('id',)
        import_id_fields = []  # Exclude id from import_id_fields to let Django generate it automatically

@admin.register(Historic_Consumption)
class HistoricConsumptionAdmin(ImportExportModelAdmin):
    resource_class = HistoricConsumptionResource
    list_display = ("consumption_date", "registration_no", "region", "fuel_type", "quantity", "cost_per_liter", "total_amount")
    search_fields = ("registration_no", "region", "fuel_type")
    readonly_fields = ("consumption_date",)

    fieldsets = (
        ('General Information', {
            'fields': ('consumption_date', 'registration_no', 'region', 'fuel_type'),
        }),
        ('Consumption Details', {
            'fields': ('quantity', 'cost_per_liter', 'total_amount'),
        }),
    )
