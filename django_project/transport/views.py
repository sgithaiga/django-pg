from urllib import request
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import ValidationError
from django.contrib.messages.views import SuccessMessageMixin
import json
from django.db.models import Count, Q
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from xhtml2pdf import pisa
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
from formtools.wizard.views import SessionWizardView
from django.utils import timezone
from django.db.models import Q
from django.core.files.storage import FileSystemStorage

from django.urls import reverse_lazy

from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  TemplateView,
                                  View)

from .models import (Vehicle_register, 
                    Driver, 
                    Request_fuel, 
                    Assign_fuel, 
                    Fuel_mgt,
                    Fuel_mgt_update, 
                    Vehicle_issues, 
                    Vehicle_handover, 
                    Fuel_price, 
                    Fuel_name,
                    station,
                    UserUnit,
                    Driver_Incidents, 
                    TestM,
                    Person,
                    City,
                    Motor_Cycle_Make,
                    Motor_Cycle_Model,
                    Generator,
                    Rider,
                    Fuel_mgt_m,
                    Fuel_mgt_xn,
                    Vendor_station,
                    Vendor_fuel_types,
                    Vendor_price,
                    ThreadModel,
                    MessageModel,
                    Notification,
                    Motor_bike_register,
                    Fuel_mgt_mb,)

from transport.forms import (Assign_fuelForm, 
                            Request_fuelForm, 
                            Vehicle_registerForm, 
                            Fuel_mgtreqForm,
                            Fuel_mgt_updatenewForm,
                            Fuel_mgt_issueForm, 
                            TestMForm,
                            FormStepOne, 
                            FormStepTwo, 
                            FormStepThree, 
                            FormStepFour, 
                            FormStepFive, 
                            FormStepSix, 
                            Fuel_mgtnewForm,
                            Driver_IncidentsForm,
                            PersonForm,
                            Fuel_mgt_xnForm,
                            Fuel_mgt_xn_issueForm,
                            BulkFuelForm,
                            DriverEditForm,
                            ThreadForm,
                            MessageForm,
                            BPOapproval_Form,
                            Motorbike_registerForm,
                            Fuel_mgt_mbForm,
                            GeneratorForm)

from .filters import RequestFilter

# Create your views here.

@login_required       
def home_view(request):
    return render(request, 'transport/transport-home.html')

#function connect to load fuel prices in the drop down 
def load_prices(request):
    fuel_name_id = request.GET.get('fuel_type_requested')
    prices = Fuel_price.objects.filter(fuel_name_id=fuel_name_id).all()
    return render(request, 'transport/prices_dropdown_list_options.html', {'prices': prices})

def load_vehicles(request):
    region_id = request.GET.get('region')
    vehicles = Vehicle_register.objects.filter(region_id=region_id).all()
    return render(request, 'transport/vehicle_dropdown_list_options.html', {'vehicles': vehicles})

def load_user_regions(request):
    region_name_id = request.GET.get('region')
    codes = UserUnit.objects.filter(region_name_id=region_name_id).all()
    return render(request, 'transport/codes_dropdown_list_options.html', {'codes': codes})

def load_vendor_location(request):
    vendor_id = request.GET.get('vendor_name')
    locations = Vendor_station.objects.filter(vendor_name_id=vendor_id).all()
    return render(request, 'transport/locations_dropdown_list_options.html', {'locations': locations})

def load_vendor_fuel_types(request):
    vendor_name_id = request.GET.get('vendor_name')
    fuel_types = Vendor_fuel_types.objects.filter(vendor_name_id=vendor_name_id).all()
    return render(request, 'transport/vendor_fuel_types_dropdown_list_options.html', {'fuel_types': fuel_types})

def load_vendor_prices(request):
    fuel_name_id = request.GET.get('fuel_type_requested')
    v_prices = Vendor_price.objects.filter(fuel_name_id=fuel_name_id).all()
    return render(request, 'transport/vendor_prices_dropdown_list_options.html', {'v_prices': v_prices})

def load_vendor_discounts(request):
    fuel_name_id = request.GET.get('fuel_type_requested')
    discounts = Vendor_price.objects.filter(fuel_name_id=fuel_name_id).all()
    return render(request, 'transport/discount_dropdown_list_options.html', {'discounts': discounts})



def fuelapproval_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    approval = get_object_or_404(Fuel_mgt_xn, pk=pk)

    template_path = 'transport/transport_pdf.html'
    context = {'approval': approval}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Fuel Approval.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



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

def index(request):  
    req = Fuel_mgtreqForm()  
    return render(request, 'transport/index.html', {'form':req})  

class Request_fuelCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):

    permission_required = 'transport.add_request_fuel'

    model = Request_fuel
    fields = ['vehicle_registration_number', 'region', 'fuel_type_requested', 'fuel_amount_requested', 'price_per_liter', 'total', 'driver_assigned']

    def form_valid(self,form):
        form.instance.requested_by = self.request.user
        return super().form_valid(form)

class Request_fueltDetailView(LoginRequiredMixin, DetailView):

    
    
    model = Request_fuel
    template_name = 'transport/Request_fuel_detail.html' #<app>/<model>_<viewtype>.html

class Request_fuelListView(LoginRequiredMixin, ListView):

    model = Request_fuel
    template_name = 'transport/Request_fuel_list.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_requested']
    paginate_by = 10

#display user requests in class list view
class UserRequest_fuelListView(LoginRequiredMixin, ListView):

    model = Request_fuel
    template_name = 'transport/Request_fuel_list_userfrm.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Request_fuel.objects.filter(requested_by=user).order_by('-date_requested')

class Request_fuel_UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    #permission_required = ('transport.view_request_fuel', 'transport.change_request_fuel')
    model = Request_fuel
    fields = ['vehicle_registration_number', 'region', 'fuel_type_requested', 'fuel_amount_requested', 'price_per_liter', 'total']

    def form_valid(self,form):
        form.instance.requested_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.requested_by:
            return True
        return False

class Request_fuelDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Request_fuel
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.requested_by:
            return True
        return False

class Request_fuelUpdate(LoginRequiredMixin, UserAccessMixin, UpdateView):

    permission_required = ('transport.view_request_fuel', 'transport.change_request_fuel')
    model = Request_fuel
    template_name = 'transport/Request_fuel_approve.html' #<app>/<model>_<viewtype>.html
    fields = ['approved', 'declined', 'reason']

    def form_valid(self,form):
        form.instance.approved_by = self.request.user
        return super().form_valid(form)

class Request_fuel_declineUpdate(LoginRequiredMixin, UserAccessMixin, UpdateView):

    permission_required = ('transport.view_request_fuel', 'transport.change_request_fuel')
    model = Request_fuel
    template_name = 'transport/Request_fuel_decline.html' #<app>/<model>_<viewtype>.html
    fields = ['declined', 'reason']

    def form_valid(self,form):
        form.instance.approved_by = self.request.user
        return super().form_valid(form)


class Request_fuel_completeUpdate(LoginRequiredMixin, UserAccessMixin, UpdateView):

    permission_required = 'transport.change_request_fuel'
    model = Request_fuel
    template_name = 'transport/Request_fuel_complete.html' #<app>/<model>_<viewtype>.html
    fields = ['fuel_issue_complete']

class Assign_fuelCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):

    permission_required = 'transport.add_assign_fuel'
    model = Assign_fuel
    fields = ['station_name', 'fuel_type', 'price_per_liter', 'liters_served', 'vehicle', 'current_mileage', 'amount', 'station']

    def form_valid(self,form):
        form.instance.entered_by = self.request.user
        return super().form_valid(form)


class Assign_fuelListView(LoginRequiredMixin, ListView):
    model = Assign_fuel
    template_name = 'transport/Assign_fuel_list.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

class Assign_fueltDetailView(LoginRequiredMixin, DetailView):
    model = Assign_fuel
    template_name = 'transport/Assign_fuel_detail.html' #<app>/<model>_<viewtype>.html

class DriverListView(LoginRequiredMixin, UserAccessMixin, ListView):
    
    permission_required = 'transport.view_driver'

    model = Driver
    template_name = 'transport/Driver_list.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'


class DriverDetailView(LoginRequiredMixin, UserAccessMixin, DetailView):
    
    permission_required = 'transport.view_driver'
    
    model = Driver
    template_name = 'transport/Driver_detail.html' #<app>/<model>_<viewtype>.html

class Vehicle_registerListView(LoginRequiredMixin, UserAccessMixin, ListView):
    
    permission_required = ('transport.view_vehicle_register')

    model = Vehicle_register
    template_name = 'transport/Vehicle_register_list.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'


class Vehicle_registerDetailView(LoginRequiredMixin, UserAccessMixin, DetailView):
    
    permission_required = 'transport.view_vehicle_register'

    model = Vehicle_register
    template_name = 'transport/Vehicle_register_detail.html' #<app>/<model>_<viewtype>.html

class Vehicle_registerCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):

    permission_required = 'transport.add_vehicle_register'

    model = Vehicle_register
    success_message = 'Vehicle successfully saved!!!!'
    template_name = 'transport/Vehicle_register_form.html' #<app>/<model>_<viewtype>.html

    form_class = Vehicle_registerForm


    def form_valid(self,form):
        form.instance.registered_by = self.request.user
        messages.success(self.request, 'Vehicle registered successfully.')
        return super().form_valid(form) 

class Vehicle_registerUpdateView(LoginRequiredMixin, UpdateView):
    #permission_required = ('transport.view_request_fuel', 'transport.change_request_fuel')
    model = Vehicle_register
    template_name = 'transport/Vehicle_register_update.html' #<app>/<model>_<viewtype>.html
    fields = ['registration_no', 'chassis_number', 'region', 'make', 'engine_capacity', 'model', 'type', 'drive_type', 'transmission', 'body_type', 'fuel_type', 'manufacture_year',
                    'fuel_tank_capacity', 'engine_no', 'color', 'vehicle_registration_date', 'gross_weight','passengers', 'tare_weight', 'tax_class', 'axles', 'load_capacity', 'operational_status', 'mechanical_status', 'remarks']

    def form_valid(self,form):
        form.instance.registered_by = self.request.user
        messages.success(self.request, 'Vehicle updated successfully.')
        return super().form_valid(form) 

class DriverCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    
    permission_required = 'transport.add_driver'

    model = Driver
    fields = ['full_name', 'pf_no', 'gender', 'region_assigned', 'license_number', 'expiry_date', 'job_title', 'driver_history', 'assigned_vehicle']
    
    def get_form(self):
        form = super().get_form()
        form.fields['expiry_date'].widget = DatePickerInput()
        return form
    def form_valid(self,form):
        form.instance.entered_by = self.request.user
        messages.success(self.request, 'Driver registered successfully.')
        return super().form_valid(form)

class DriverUpdateView(LoginRequiredMixin, UpdateView):

    #permission_required = ('transport.view_request_fuel', 'transport.change_request_fuel')
    model = Driver
    template_name = 'transport/Driver_update.html' #<app>/<model>_<viewtype>.html
    form_class = DriverEditForm

    def form_valid(self,form):
        form.instance.approved_by = self.request.user
        messages.success(self.request, 'Driver updated successfully.')
        return super().form_valid(form)

class Vehicle_issuesCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    
    permission_required = 'transport.add_vehicle_issues'

    model = Vehicle_issues
    fields = ['Vehicle_issue_topic', 'region', 'driver_assigned', 'vehicle_registration_number', 'vehicle_issue']

    def form_valid(self,form):
        form.instance.created_by = self.request.user
        messages.success(self.request, 'Vehicle issue registered successfully.')
        return super().form_valid(form)

class Vehicle_issuesListView(LoginRequiredMixin, UserAccessMixin, ListView):
    
    permission_required = 'transport.view_vehicle_issues'

    model = Vehicle_issues
    template_name = 'transport/Vehicle_issues_list.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_created']
    paginate_by = 10

class Vehicle_issuesUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    permission_required = ('transport.view_request_fuel', 'transport.change_request_fuel')
    model = Vehicle_issues
    template_name = 'transport/Vehicle_issues_wt.html' #<app>/<model>_<viewtype>.html
    fields = ['works_description', 'further_works_required_remarks', 'works_total']

    def form_valid(self,form):
        form.instance.approve_works = self.request.user
        messages.info(self.request, 'Vehicle issue updated successfully.')
        return super().form_valid(form)

class FormWizardView(SessionWizardView):
    model = Vehicle_handover
    template_name = "transport/vehicle_handover.html"
    form_list = [FormStepOne, FormStepTwo, FormStepThree, FormStepFour, FormStepFive, FormStepSix]

    def done(self, form_list, **kwargs):
        return render(self.request, 'transport/vehicle_handover_done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


class Fuel_mgtCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    
    permission_required = 'transport.add_fuel_mgt'

    model = Fuel_mgt
    form_class = Fuel_mgtnewForm
    #success_message = 'Request successfully saved!'    

    def form_valid(self, form):
        form.instance.requested_by = self.request.user
        return super().form_valid(form)
        messages.success(self.request, 'Form submission successful')

class Fuel_mgtDetailView(LoginRequiredMixin, UserAccessMixin, DetailView):

    permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')
    
    model = Fuel_mgt
    template_name = 'transport/Request_fuel_detail.html' #<app>/<model>_<viewtype>.html

class Fuel_mgtUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):

    permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')

    model = Fuel_mgt
    template_name = 'transport/Request_fuel_approve.html' #<app>/<model>_<viewtype>.html
    fields = ['approved', 'declined', 'reason']

    def form_valid(self,form):
        form.instance.approved_by = self.request.user
        return super().form_valid(form)
          

class Fuel_mgtListView(LoginRequiredMixin, UserAccessMixin, ListView):

    permission_required = 'transport.view_fuel_mgt'

    model = Fuel_mgt
    template_name = 'transport/Fuel_mgt_list.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_requested']
    paginate_by = 10

class UserFuel_mgtListView(LoginRequiredMixin, UserAccessMixin, ListView):

    model = Fuel_mgt
    template_name = 'transport/Request_fuel_list_userfrm.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Request_fuel.objects.filter(requested_by=user).order_by('-date_requested')

class Fuel_mgt_UpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')
    model = Fuel_mgt
    form_class = Fuel_mgtnewForm 

    def form_valid(self,form):
        form.instance.requested_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.requested_by:
            return True
        return False

class Fuel_mgt_declineUpdate(LoginRequiredMixin, UserAccessMixin, UpdateView):

    permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')
    model = Fuel_mgt
    template_name = 'transport/Request_fuel_decline.html' #<app>/<model>_<viewtype>.html
    fields = ['declined', 'reason']

    def form_valid(self,form):
        form.instance.approved_by = self.request.user
        return super().form_valid(form)

class Fuel_mgt_completeUpdate(LoginRequiredMixin, UserAccessMixin, UpdateView):

    permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')
    model = Fuel_mgt
    template_name = 'transport/Request_fuel_complete.html' #<app>/<model>_<viewtype>.html
    fields = ['fuel_issue_complete']


class Fuel_mgtDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    permission_required = 'transport.delete_fuel_mgt'
    model = Fuel_mgt
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.requested_by:
            return True
        return False

#fuel issue views

class Fuel_mgt_f_issue_UpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):

    permission_required = 'transport.change_fuel_mgt'
    model = Fuel_mgt
    form_class = Fuel_mgt_issueForm
    template_name = 'transport/fuel_mgt_issue.html'
    #fields = ['fuel_station_name', 'liters_served', 'amount', 'station_mileage']

    def form_valid(self,form):
        form.instance.attended_by = self.request.user
        return super().form_valid(form)

#driver incident recording and list views
class Driver_IncidentsCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    
    permission_required = 'transport.add_driver_incidents'
    model = Driver_Incidents
    form_class = Driver_IncidentsForm    

    def form_valid(self, form):
        form.instance.registered_by = self.request.user
        messages.success(self.request, 'Driver incident registered successfully.')
        return super().form_valid(form)   

class Driver_IncidentsListView(LoginRequiredMixin, UserAccessMixin, ListView):
    
    permission_required = 'transport.view_fuel_mgt'

    model = Driver_Incidents
    template_name = 'transport/Driver_Incidents_list.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_logged']
      
    
#garage operations
class Vehicle_issuesDetailView(LoginRequiredMixin, UserAccessMixin, DetailView):

    #permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')
    
    model = Vehicle_issues
    template_name = 'transport/Mech_assesment_detail.html' #<app>/<model>_<viewtype>.html
 

class mechanic_assesmentUpdate(LoginRequiredMixin, UpdateView):
    model = Vehicle_issues
    fields = ['vehicle_in', 'service', 'repair', 'current_mileage', 'next_service', 'mechanic_assesment']
    template_name = 'transport/Mech_assessment.html'

    def form_valid(self, form):
        form.instance.mechanic = self.request.user
        messages.success(self.request, 'Mechanic assessment updated successfully.')
        return super().form_valid(form) 

class work_assessmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle_issues
    fields = ['check_report', 'works_description', 'parts_required', 'works_total']
    template_name = 'transport/work_assessment.html'

    def form_valid(self, form):
        form.instance.transport_assistant = self.request.user
        messages.info(self.request, 'work assessmebt updated successfully.')
        return super().form_valid(form)

class work_assessment_approvalUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle_issues
    fields = ['approve_works']
    template_name = 'transport/work_assessment_approval.html'

    def form_valid(self, form):
        form.instance.transport_officer = self.request.user
        messages.info(self.request, 'Works approval updated successfully.')
        return super().form_valid(form) 

class work_assessmentDetailView(LoginRequiredMixin, DetailView):

    #permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')
    
    model = Vehicle_issues
    template_name = 'transport/Work_assesment_detail.html' #<app>/<model>_<viewtype>.html    
#views for testing linkedlists

class PersonListView(ListView):
    model = Person
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'transport/list.html'

    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = Person
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changelist')

#return a list of cities for any given country
def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'transport/city_dropdown_list_options.html', {'cities': cities})

#test multiplication of fields and adding into a third field
class TestMCreateView(CreateView):
    
    model = TestM
    template_name = 'transport/test_m.html' #<app>/<model>_<viewtype>.html
    form_class = TestMForm
    success_message = 'Request successfully saved!'    

    def form_valid(self, form):
        return super().form_valid(form)

def total(request):
    a = request.GET['price']
    b = request.GET['quantity']
    c = a*b

    return render(request, 'transport/output.html', {'result':c})

class TestMListView(ListView):
    

    model = TestM
    template_name = 'transport/Test_M_list.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10  

class Fuel_mgt_updateCreateView(CreateView):
    
    model = Fuel_mgt
    template_name = 'transport/Fuel_mgt_updated.html' #<app>/<model>_<viewtype>.html
    form_class = Fuel_mgt_updatenewForm
    success_message = 'Request successfully saved!'    

    def form_valid(self, form):
        form.instance.requested_by = self.request.user
        return super().form_valid(form) 

#view for filtering
def Reqfilter(request):
    fuel_req = Fuel_mgt.objects.all()
    myFilter = RequestFilter(request.GET, queryset=fuel_req)
    fuel_req = myFilter.qs
    context = {
        'myFilter': myFilter,
        'fuel_req': fuel_req,
    }
    return render(request, 'transport/req_filter.html', context)

#motor cycles
class Motorcycle_CreateView(LoginRequiredMixin, CreateView):


    model = Motor_Cycle_Model
    template_name = 'transport/Motorcycle_register_form.html' #<app>/<model>_<viewtype>.html
    fields = ['motor_cycle_make', 'Motor_cycle_model', 'motor_cycle_reg_no', 'region', 'fuel_type', 'fuel_capacity', 'engine_no']


    def form_valid(self,form):
        form.instance.entered_by = self.request.user
        messages.success(self.request, 'Motorcycle created successfully.')
        return super().form_valid(form)



class Rider_CreateView(LoginRequiredMixin, CreateView):


    model = Rider
    template_name = 'transport/Motorcycle_Rider_register_form.html' #<app>/<model>_<viewtype>.html
    fields = ['full_name', 'pf_no', 'region_assigned', 'assigned_motorcycle']


    def form_valid(self,form):
        form.instance.entered_by = self.request.user
        messages.success(self.request, 'Rider created successfully.')
        return super().form_valid(form)

class Rider_ListView(LoginRequiredMixin, ListView):
    
    model = Rider
    template_name = 'transport/Rider_list.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'

class Generator_CreateView(LoginRequiredMixin, CreateView):


    model = Generator
    template_name = 'transport/Generator_register_form.html' #<app>/<model>_<viewtype>.html
    # fields = ['serial_number', 'make', 'model', 'location', 'output']
    form_class = GeneratorForm


    def form_valid(self,form):
        form.instance.entered_by = self.request.user
        messages.success(self.request, 'Generator created successfully.')
        return super().form_valid(form)

class Generator_ListView(LoginRequiredMixin, ListView):
    
    model = Generator
    template_name = 'transport/Generator_list.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'

###############validation views for Fuel_mgt_xnForm
def validateStatus(request, pk):
    # Vehicle_register = get_object_or_404(Vehicle_register, pk=pk)
    if request.method == "GET":
        try:
            queryset = Vehicle_register.objects.filter(pk=pk, operational_status='grounded').values()

            if queryset:
                raise ValidationError(f'This vehicle is listed as grounded and cannot be fueled. Kindly review your selection or contact the fleet administrator for assistance')    
            data = list(queryset.values())
            return JsonResponse(data, safe=False)
        except ValidationError as e:
            error_message = str(e)
            return JsonResponse({'error': error_message}, status=400)

class LoadVehicleType(View):
    def get(self, request):
        vehicle_id = request.GET.get('registration_no')
        try:
            vehicle = Vehicle_register.objects.get(id=vehicle_id)
            vehicle_type = vehicle.type
            return JsonResponse({'vehicle_type': vehicle_type})
        except Vehicle_register.DoesNotExist:
            return JsonResponse({'error': 'Vehicle with this ID does not exist'}, status=404)


############################# new form xn views


class Fuel_mgt_mCreateView(LoginRequiredMixin,  View):
    # permission_required = 'transport.add_fuel_mgt'UserAccessMixin,
    template_name = 'transport/fuel_mgt_m_form.html'

    def get(self, request, *args, **kwargs):
        form = Fuel_mgt_xnForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = Fuel_mgt_xnForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Get the vehicle for which the fuel request is being made
                vehicle = get_object_or_404(Vehicle_register, registration_no=form.instance.registration_no)

                # Get the last fuel request for this vehicle
                last_fuel_request = Fuel_mgt_xn.objects.filter(registration_no=vehicle).order_by('-date_requested').first()

                if last_fuel_request:
                    # Set the previous mileage and liters served to the current mileage and liters served of the last fuel request
                    form.instance.previous_mileage = last_fuel_request.current_mileage
                    form.instance.previous_liters_served = last_fuel_request.liters_served

                form.instance.requested_by = self.request.user
                form.save()
                messages.success(self.request, 'Fuel request created successfully.')
                return redirect('fuel-mgtm-list')  # replace 'success_url' with the actual success url
            except Http404:
                form.add_error('registration_no', 'Vehicle with this registration number does not exist.')
            except ValidationError as e:
                # Add the error to the form's errors
                form.add_error(None, e)   
        return render(request, self.template_name, {'form': form})



class Fuel_mgt_mListView(LoginRequiredMixin, ListView):

    #permission_required = 'transport.view_fuel_mgt'

    model = Fuel_mgt_xn
    template_name = 'transport/Fuel_mgt_xnlist.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_requested']
 
def taskList(request):
  user_tasks =Fuel_mgt_xn.objects.filter(assign_request=request.user)
#   tasks = Fuel_mgt_xn.objects.filter(assignee=None) 'tasks':tasks, 
  context = {'user_tasks':user_tasks}
  return render(request, 'transport/user_tasks.html',context)  

class Fuel_mgt_mDetailView(LoginRequiredMixin, DetailView):

    #permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')
    
    model = Fuel_mgt_xn
    template_name = 'transport/Fuel_mgt_xn_detail.html' #<app>/<model>_<viewtype>.html

class Fuel_mgt_mUpdateView(LoginRequiredMixin, UpdateView):

    #permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')

    model = Fuel_mgt_xn
    template_name = 'transport/Fuel_mgt_xn_approve.html' #<app>/<model>_<viewtype>.html
    fields = ['approved', 'declined', 'assign_request']

    def form_valid(self,form):
        form.instance.approved_by = self.request.user
        messages.info(self.request, 'Fuel Request status updated successfully.')
        return super().form_valid(form)

class Fuel_mgt_mcompleteUpdate(LoginRequiredMixin, UpdateView):

    #permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')
    model = Fuel_mgt_xn
    template_name = 'transport/Fuel_mgt_xn_complete.html' #<app>/<model>_<viewtype>.html
    fields = ['fuel_issue_complete'] 

class Fuel_mgtmDeleteView(LoginRequiredMixin, DeleteView):

    #permission_required = 'transport.delete_fuel_mgt'
    model = Fuel_mgt_xn
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.requested_by:
            return True
        return False

class Fuel_mgtm_declineUpdate(LoginRequiredMixin, UpdateView):

    #permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')
    model = Fuel_mgt_xn
    template_name = 'transport/Fuel_mgt_xn_decline.html' #<app>/<model>_<viewtype>.html
    fields = ['declined', 'reason']

    def form_valid(self,form):
        form.instance.approved_by = self.request.user
        return super().form_valid(form) 

#fuel issue views

class Fuel_mgtm_f_issue_UpdateView(LoginRequiredMixin, UpdateView):

    #permission_required = 'transport.change_fuel_mgt'
    model = Fuel_mgt_xn
    form_class = Fuel_mgt_xn_issueForm
    template_name = 'transport/Fuel_mgt_xn_issue.html'
    #fields = ['fuel_station_name', 'liters_served', 'amount', 'station_mileage']

    def form_valid(self,form):
        form.instance.attended_by = self.request.user
        messages.success(self.request, 'Fuel issuance completed successfully.')

        return super().form_valid(form)

class Fuel_mgtmDetailView(LoginRequiredMixin, DetailView):

    #permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')
    
    model = Fuel_mgt_xn
    template_name = 'transport/Fuel_mgt_xn_detail.html' #<app>/<model>_<viewtype>.html

class UserFuel_mgmtListView(LoginRequiredMixin, ListView):

    model = Fuel_mgt_xn
    template_name = 'transport/Fuel_mgt_xn_list_userfrm.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Fuel_mgt_xn.objects.filter(requested_by=user).order_by('-date_requested')

class Fuel_mgt_mBPOUpdateView(LoginRequiredMixin, UpdateView):

    #permission_required = ('transport.view_fuel_mgt', 'transport.change_fuel_mgt')

    model = Fuel_mgt_xn
    template_name = 'transport/Fuel_mgt_xn_BPOapprove.html' #<app>/<model>_<viewtype>.html
    form_class = BPOapproval_Form

    def form_valid(self,form):
        form.instance.approved_by_BPO = self.request.user
        messages.info(self.request, 'Fuel Request status updated successfully.')
        return super().form_valid(form)
    
#messaging
class CreateThread(View):
  def get(self, request, *args, **kwargs):
    form = ThreadForm()
    context = {
      'form': form
    }
    return render(request, 'transport/create_thread.html', context)
  def post(self, request, *args, **kwargs):
    form = ThreadForm(request.POST)
    username = request.POST.get('username')
    try:
      receiver = User.objects.get(username=username)
      if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
        thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
        return redirect('thread', pk=thread.pk)
      
      if form.is_valid():
        sender_thread = ThreadModel(
          user=request.user,
          receiver=receiver
        )
        sender_thread.save()
        thread_pk = sender_thread.pk
        return redirect('thread', pk=thread_pk)
    except:
      return redirect('create-thread') 

class ListThreads(View):
  def get(self, request, *args, **kwargs):
    threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))
    context = {
        'threads': threads
    }
    return render(request, 'transport/inbox.html', context) 
  
class CreateMessage(View):
  def post(self, request, pk, *args, **kwargs):
    thread = ThreadModel.objects.get(pk=pk)
    if thread.receiver == request.user:
      receiver = thread.user
    else:
      receiver = thread.receiver
      message = MessageModel(
        thread=thread,
        sender_user=request.user,
        receiver_user=receiver,
        body=request.POST.get('message'),
      )
      message.save()
      return redirect('thread', pk=pk)

class ThreadView(View):
  def get(self, request, pk, *args, **kwargs):
    form = MessageForm()
    thread = ThreadModel.objects.get(pk=pk)
    message_list = MessageModel.objects.filter(thread__pk__contains=pk)
    context = {
      'thread': thread,
      'form': form,
      'message_list': message_list
    }
    return render(request, 'transport/thread.html', context)

####register motor cycle

class Motorbike_registerCreateView(CreateView):

    model = Motor_bike_register
    template_name = 'transport/Motorbike_register_form.html' #<app>/<model>_<viewtype>.html

    form_class = Motorbike_registerForm


    def form_valid(self,form):
        form.instance.registered_by = self.request.user
        messages.success(self.request, 'Motorcycle registered successfully.')
        return super().form_valid(form) 
    
class Motorcycle_ListView(LoginRequiredMixin, ListView):
    
    model = Motor_bike_register
    template_name = 'transport/Motorcycle_list.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_registered']
    
    
###### motorbike fuel request management

class Fuel_mgt_mbikeCreateView(LoginRequiredMixin, CreateView):
    
    # permission_required = 'transport.add_fuel_mgt' UserAccessMixin, 

    model = Fuel_mgt_mb
    form_class = Fuel_mgt_mbForm
    template_name = 'transport/fuel_mgt_mbike_form.html'
    #success_message = 'Request successfully saved!'    

    def form_valid(self, form):
        form.instance.requested_by = self.request.user
        messages.success(self.request, 'Fuel request created successfully.')
        return super().form_valid(form)

