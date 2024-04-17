from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, UpdateView, FormView)
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login

from .models import Vehicle, Parts, TyreIssuance, ImprestPartsAquisition, VehicleDispatch
from .forms import partsrequestForm, patsrequestEditForm, TyreIssuanceForm, ImprestPartsAquisitionForm, ImprestPartsAquisitionUpdateForm, VehicleDispatchForm, VehicleDispatchUpdateForm
# VehiclePartsFormset

class UserAccessMixin(PermissionRequiredMixin):

    #check if user is logged in
    def dispatch(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path,
                                    self.get_login_url(), self.get_redirect_field_name())
        #check if user has permissions
        if not self.has_permission():
            return redirect('/error/')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)
        
class PermissionsView(TemplateView):
    template_name = "transport/permissions_error.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'parts/home.html'


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'parts/vehicle_list.html'


class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'parts/vehicle_detail.html'


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = 'parts/vehicle_create.html'
    fields = ['registration_number', 'order',]

    def form_valid(self, form):
        form.instance.ordered_by = self.request.user

        messages.add_message(
            self.request, 
            messages.SUCCESS,
            'The vehicle has been added'
        )

        return super().form_valid(form)

# class VehiclePartsEditView(LoginRequiredMixin, SingleObjectMixin, FormView):

#     model = Vehicle
#     template_name = 'parts/vehicle_parts_edit.html'

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object(queryset=Vehicle.objects.all())
#         return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object(queryset=Vehicle.objects.all())
#         return super().post(request, *args, **kwargs)

#     def get_form(self, form_class=None):
#         return VehiclePartsFormset(**self.get_form_kwargs(), instance=self.object)

#     def form_valid(self, form):
#         form.save()

#         messages.add_message(
#             self.request,
#             messages.SUCCESS,
#             'Changes were saved.'
#         )

#         return HttpResponseRedirect(self.get_success_url())

#     def get_success_url(self):
#         return reverse('parts:vehicle_detail', kwargs={'pk': self.object.pk})

class VehiclePartsListView(LoginRequiredMixin, ListView):
    model = Parts
    template_name = 'parts/vehicle_parts_list.html'
    
class partsrequestView(CreateView):
    model = Parts
    form_class = partsrequestForm
    template_name = 'parts/parts_request.html'
    success_url = reverse_lazy('parts:list-parts') 
    
class partsrequestDetailView(LoginRequiredMixin, DetailView):

    #permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')  
    model = Parts
    template_name = 'parts/partrequest_detail.html' #<app>/<model>_<viewtype>.html

class partsrequestUpdateView(UpdateView):
    model = Parts
    template_name = 'parts/partsrequest_update.html'
    form_class = patsrequestEditForm

    def form_valid(self, form):
        form.instance.approved_by = self.request.user
        messages.success(self.request, 'Part request updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('parts:list-parts')
        
def home_view(request):
    return render(request, 'transport/parts/parts-home.html')

class TyreIssuanceCreateView(CreateView):
    model = TyreIssuance
    form_class = TyreIssuanceForm
    template_name = 'parts/tyre_issuance_form.html'  # Replace with your template name
    success_url = reverse_lazy('parts:list-tyre-issuance') # Replace with your success URL

    def form_valid(self, form):
        form.instance.issued_by = self.request.user  # Set issued_by to the current user
        return super().form_valid(form)
    
class TyreIssuanceListView(ListView):
    model = TyreIssuance
    template_name = 'parts/tyre_issuance_list.html'  # Replace with your template name
    context_object_name = 'tyre_issuances'  # This will be the variable name in the template
    
class ImprestPartsAquisitionCreateView(CreateView):
    model = ImprestPartsAquisition
    form_class = ImprestPartsAquisitionForm
    template_name = 'parts/ImprestPartsAquisition_form.html'  # Replace with your template name
    success_url = reverse_lazy('parts:list-imperest-requests') # Replace with your success URL

    def form_valid(self, form):
        form.instance.requested_by = self.request.user  # Set issued_by to the current user
        return super().form_valid(form)
    
class ImprestPartsAquisitionListView(ListView):
    model = ImprestPartsAquisition
    template_name = 'parts/ImprestPartsAquisition_list.html'  # Replace with your template name
    context_object_name = 'ip_requests'  # This will be the variable name in the template
    
class ImprestPartsAquisitiontUpdateView(UpdateView):
    model = ImprestPartsAquisition
    template_name = 'parts/ImprestPartsAquisition_update.html'
    form_class = ImprestPartsAquisitionUpdateForm

    def form_valid(self, form):
        form.instance.approved_by = self.request.user
        messages.success(self.request, 'Part request updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('parts:list-imperest-requests')

class ImprestPartsAquisitionDetailView(LoginRequiredMixin, DetailView):

    #permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')  
    model = ImprestPartsAquisition
    template_name = 'parts/ImprestPartsAquisition_detail.html' #<app>/<model>_<viewtype>.html
    
class VehicleDispatchCreateView(CreateView):
    model = VehicleDispatch
    form_class = VehicleDispatchForm
    template_name = 'parts/VehicleDispatchForm_form.html'  # Replace with your template name
    success_url = reverse_lazy('parts:garage-dipatch-list') # Replace with your success URL

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Set issued_by to the current user
        messages.success(self.request, 'Dispatch requested created successfully.')
        return super().form_valid(form)

# class VehicleDispatchUpdateView(CreateView):
#     model = VehicleDispatch
#     form_class = VehicleDispatchUpdateForm
#     template_name = 'parts/VehicleDispatchUpdateForm_form.html'  # Replace with your template name
#     success_url = reverse_lazy('parts:garage-dipatch-list') # Replace with your success URL

#     def form_valid(self, form):
#         form.instance.updated_by = self.request.user  # Set issued_by to the current user
#         messages.success(self.request, 'Dispatch requested updated successfully.')
#         return super().form_valid(form)

class VehicleDispatchUpdateView(LoginRequiredMixin, UpdateView):
    model = VehicleDispatch
    form_class = VehicleDispatchUpdateForm
    template_name = 'parts/VehicleDispatchUpdateForm_form.html'
    success_url = reverse_lazy('parts:garage-dipatch-list')

    def form_valid(self, form):
        try:
            form.instance.updated_by = self.request.user
            # Set registration_no here
            form.instance.registration_no = form.cleaned_data['registration_no']
            messages.success(self.request, 'Dispatch request updated successfully.')
            return super().form_valid(form)
        except Http404:
            form.add_error(None, 'Vehicle with this registration number does not exist.')
            return self.form_invalid(form)
        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)  
class VehicleDispatchListView(ListView):
    model = VehicleDispatch
    template_name = 'parts/VehicleDispatch_list.html'  # Replace with your template name
    context_object_name = 'dispatchs'  # This will be the variable name in the template

