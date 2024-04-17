from django import forms
from django.forms.widgets import DateInput
from django.utils.translation import ugettext_lazy as _
from .models import NTSACompliance, InsuranceCompliance

class NTSAComplianceForm(forms.ModelForm):
    class Meta:
        model = NTSACompliance
        exclude = ('last_inspection_date', 'total_fees')
        labels = {
            'registration_no': 'Vehicle Registration Number',
            'inspection_date': 'Inspection Date',
            'next_inspection_date': 'Next Inspection Date',
            'inspection_sticker_issued_date': 'Sticker Issuance Date',
            'inspection_sticker_expiry_date': 'Sticker Expiry Date',
            'booking_fee': 'Booking Fee',
            'inspection_fee': 'Inspection Fee',
        }
        widgets = {
            'inspection_date': forms.DateInput(attrs={'type': 'date'}),
            'next_inspection_date': forms.DateInput(attrs={'type': 'date'}),
            'inspection_sticker_issued_date': forms.DateInput(attrs={'type': 'date'}),
            'inspection_sticker_expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

class NTSAComplianceUpdateForm(forms.ModelForm):
    class Meta:
        model = NTSACompliance
        exclude = ['registration_no']
        labels = {
            'inspection_date': 'Inspection Date',
            'next_inspection_date': 'Next Inspection Date',
            'inspection_sticker_issued_date': 'Sticker Issuance Date',
            'inspection_sticker_expiry_date': 'Sticker Expiry Date',
            'booking_fee': 'Booking Fee',
            'inspection_fee': 'Inspection Fee',
        }
        widgets = {
            'inspection_date': forms.DateInput(attrs={'type': 'date'}),
            'next_inspection_date': forms.DateInput(attrs={'type': 'date'}),
            'inspection_sticker_issued_date': forms.DateInput(attrs={'type': 'date'}),
            'inspection_sticker_expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

        

class InsuranceComplianceForm(forms.ModelForm):
    class Meta:
        model = InsuranceCompliance
        fields = ['vehicle', 'insurance_provider', 'date_policy_issued', 'date_policy_expiry', 'insurance_fee']
        labels = {
            'vehicle': _('Vehicle'),
            'insurance_provider': _('Insurance Provider'),
            'date_policy_issued': _('Date Policy Issued'),
            'date_policy_expiry': _('Date Policy Expiry'),
            'insurance_fee': _('Insurance Fee'),
        }
        widgets = {
            'date_policy_issued': DateInput(attrs={'type': 'date'}),
            'date_policy_expiry': DateInput(attrs={'type': 'date'}),
        }
        
class InsuranceComplianceUpdateForm(forms.ModelForm):
    class Meta:
        model = InsuranceCompliance
        exclude = ['vehicle']
        labels = {
            'insurance_provider': _('Insurance Provider'),
            'date_policy_issued': _('Date Policy Issued'),
            'date_policy_expiry': _('Date Policy Expiry'),
            'insurance_fee': _('Insurance Fee'),
        }
        widgets = {
            'date_policy_issued': DateInput(attrs={'type': 'date'}),
            'date_policy_expiry': DateInput(attrs={'type': 'date'}),
        }
