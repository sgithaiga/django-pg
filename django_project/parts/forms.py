# from django.forms.models import inlineformset_factory
from django import forms
from django.forms.widgets import DateInput

from .models import Vehicle, Parts, TyreIssuance, ImprestPartsAquisition, VehicleDispatch

# VehiclePartsFormset = inlineformset_factory(Vehicle, Parts, fields=('title', 'quantity', 'delivered', 'fitted',))

class partsrequestForm(forms.ModelForm):

    class Meta:
        model = Parts
        fields = ('part_name', 'serial_number', 'registration_number', 'quantity', 'delivered', 'date_delivered', 'fitted', 'date_fitted')
        
        widgets = {
            'date_delivered': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'date_fitted': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

class patsrequestEditForm(forms.ModelForm):
    
    class Meta:
        model = Parts
        fields = '__all__'
        
        widgets = {
            'date_delivered': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'date_fitted': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

class TyreIssuanceForm(forms.ModelForm):
    class Meta:
        model = TyreIssuance
        exclude = ['issued_by', 'date_issued']  # Exclude these fields from the form


class ImprestPartsAquisitionForm(forms.ModelForm):
    class Meta:
        model = ImprestPartsAquisition
        fields = ('station', 'registration_no', 'part_category', 'part_name', 'part_cost', 'quantity', 'invoice', 'invoice_no', 'vendor')
        # exclude = ['requested_by', 'date_requested','approve_requisition', 'date_approved', 'approved_by']  # Exclude these fields from the form

class ImprestPartsAquisitionUpdateForm(forms.ModelForm):
    class Meta:
        model = ImprestPartsAquisition
        fields = ('approve_requisition',)

class VehicleDispatchForm(forms.ModelForm):

    class Meta:
        model = VehicleDispatch
        fields = ('registration_no', 'auto_garage', 'garage_name', 'date_dispatched', 'authorization_memo')
        
        widgets = {
            'date_dispatched': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

class VehicleDispatchUpdateForm(forms.ModelForm):

    class Meta:
        model = VehicleDispatch
        fields = ('date_vehicle_received', 'service_invoice')
        
        widgets = {
            'date_vehicle_received': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }