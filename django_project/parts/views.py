from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login

from .models import Vehicle, Parts
from .forms import VehiclePartsFormset


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

class VehiclePartsEditView(LoginRequiredMixin, SingleObjectMixin, FormView):

    model = Vehicle
    template_name = 'parts/vehicle_parts_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Vehicle.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Vehicle.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return VehiclePartsFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('parts:vehicle_detail', kwargs={'pk': self.object.pk})

class VehiclePartsListView(LoginRequiredMixin, ListView):
    model = Parts
    template_name = 'parts/vehicle_parts_list.html'

def home_view(request):
    return render(request, 'transport/parts/parts-home.html')