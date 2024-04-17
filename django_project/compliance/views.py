from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, UpdateView, FormView)
from .models import NTSACompliance, InsuranceCompliance
from .forms import NTSAComplianceForm, InsuranceComplianceForm, NTSAComplianceUpdateForm, InsuranceComplianceUpdateForm # Assuming you've created the form


# Create your views here.
class NTSAComplianceCreateView(CreateView):
    model = NTSACompliance
    form_class = NTSAComplianceForm
    template_name = 'compliance/ntsa_booking.html'  # Specify your template path
    success_url = reverse_lazy('ntsa-compliance-list')   # Redirect to this URL after successful form submission

# class NTSAComplianceListView(ListView):
#     model = NTSACompliance
#     template_name = 'compliance/ntsa_compliance_list.html'  
#     context_object_name = 'compliance_records' 
#     ordering = ['-inspection_date']

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in the current date
#         context['now'] = timezone.now()
#         return context

class NTSAComplianceListView(ListView):
    model = NTSACompliance
    template_name = 'compliance/ntsa_compliance_list.html'  
    context_object_name = 'compliance_records' 
    ordering = ['-inspection_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        thirty_days_from_today = today + timedelta(days=30)
        #print("Thirty days from today:", thirty_days_from_today)
        context['thirty_days_from_today'] = thirty_days_from_today
        return context

    
class InsuranceComplianceCreateView(CreateView):
    model = InsuranceCompliance
    form_class = InsuranceComplianceForm
    template_name = 'compliance/insurance_compliance_form.html'  # Specify your own template name
    success_url = reverse_lazy('insurance-compliance-list')  # URL to redirect to after successful creation

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user  # Assuming you want to save the user who created the object
    #     return super().form_valid(form)
    
class InsuranceComplianceListView(ListView):
    model = InsuranceCompliance
    template_name = 'compliance/insurance_compliance_list.html'
    context_object_name = 'insurance_records'
    ordering = ['-date_policy_issued']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        thirty_days_from_today = today + timedelta(days=30)
        print("Thirty days from today:", thirty_days_from_today)
        context['thirty_days_from_today'] = thirty_days_from_today
        return context
    
class NTSAComplianceUpdateView(UpdateView):

    #permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')

    model = NTSACompliance
    template_name = 'compliance/NTSAcomplianceupdate.html' #<app>/<model>_<viewtype>.html
    form_class = NTSAComplianceUpdateForm

    # def form_valid(self,form):
    #     form.instance.updated_by = self.request.user
    #     messages.info(self.request, 'Compliance status updated successfully.')
    #     return super().form_valid(form)
    
class InsuranceComplianceUpdateView(UpdateView):

    #permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')

    model = InsuranceCompliance
    template_name = 'compliance/Insurancecomplianceupdate.html' #<app>/<model>_<viewtype>.html
    form_class = InsuranceComplianceUpdateForm

    # def form_valid(self,form):
    #     form.instance.updated_by = self.request.user
    #     messages.info(self.request, 'Compliance status updated successfully.')
    #     return super().form_valid(form)