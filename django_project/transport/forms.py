from django.forms import fields
from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.forms.widgets import NumberInput, DateInput
from .models import (Assign_fuel, 
                    Request_fuel, 
                    Vehicle_register, 
                    Driver, 
                    Fuel_mgt,
                    Fuel_mgt_update, 
                    Vehicle_issues, 
                    Vehicle_handover, 
                    station, 
                    Fuel_name, 
                    Fuel_price,
                    Driver_Incidents, 
                    Person, 
                    City,
                    TestM,
                    Fuel_mgt_m,
                    Model,
                    Vendor_price,
                    Vendor_station,
                    Vendor_fuel_types,
                    Fuel_mgt_xn,
                    Motor_bike_make,
                    Motor_bike_model,
                    Motor_bike_register,
                    Fuel_mgt_mb)
from django.utils import timezone
from django.forms import DateInput
from django.db.models import Q


APPROVAL_STATUS= [
    ('approved', 'Approved'),
    ('declined', 'Declined'),
    ]
class Assign_fuelForm(forms.ModelForm):

    class Meta:
        model = Assign_fuel
        fields = ('station_name', 'fuel_type', 'price_per_liter', 'liters_served', 
        	       'previous_liters_served', 'vehicle', 'current_mileage', 'amount', 'station')

class Request_fuelForm(forms.ModelForm):

    class Meta:
        model = Request_fuel
        fields = ('vehicle_registration_number', 'region', 'fuel_type_requested', 'price_per_liter',
                     'fuel_amount_requested', 'total', 'date_requested', 'driver_assigned')
    

class Vehicle_registerForm(forms.ModelForm):
    class Meta:
        model = Vehicle_register
        fields = ('registration_no', 'chassis_number', 'region', 'make', 'engine_capacity', 'model', 'type', 'drive_type', 'transmission', 'body_type', 'fuel_type', 'manufacture_year',
                    'fuel_tank_capacity', 'engine_no', 'color', 'vehicle_registration_date', 'gross_weight','passengers', 'tare_weight', 'tax_class', 'axles', 'load_capacity', 'operational_status', 'mechanical_status', 'remarks')

        widgets = {'manufacture_year': DateInput( format=('%Y-%m-%d'), 
               attrs={'type': 'date' }),
               }
class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('full_name', 'pf_no', 'gender', 'region_assigned', 'license_number', 'expiry_date', 'driver_history', 'assigned_vehicle')
        

        widgets = {'expiry_date': DateInput( format=('%Y-%m-%d'), 
               attrs={'type': 'date' }),
               }

class DriverEditForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ('region_assigned', 'license_number', 'job_title', 'driver_history', 'assigned_vehicle')



class requestSearchForm(forms.Form):
        search_text =  forms.CharField(
                    required = False,
                    label='Search for vehicle',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )
        
        search_name = forms.CharField(
                    required = False,
                    label='Search name!',
                    widget=forms.TextInput(attrs={'placeholder': 'search here!'})
                  )

class Fuel_mgtreqForm(forms.Form):

    region = forms.ModelChoiceField(queryset=station.objects.all(), widget=forms.Select(attrs={'class': ''}))
    registration_no = forms.ModelChoiceField(queryset=Vehicle_register.objects.all(), widget=forms.Select(attrs={'class': ''}))
    fuel_type_requested = forms.ModelChoiceField(queryset=Fuel_name.objects.all(), widget=forms.Select(attrs={'class': ''}))
    price_per_liter = forms.ModelChoiceField(queryset=Fuel_price.objects.all(), widget=forms.Select(attrs={'class': ''}))
    fuel_amount_requested = forms.DecimalField(label="Enter fuel amount")
    total = forms.DecimalField(widget = forms.TextInput, label="Total")
    driver_name = forms.ModelChoiceField(queryset=Driver.objects.all(), widget=forms.Select(attrs={'class': ''}))
    current_mileage = forms.CharField(widget = forms.TextInput, label="Enter current mileage", max_length=50)


class Fuel_mgtnewForm(forms.ModelForm):

    class Meta:
        model = Fuel_mgt
        fields = ('region', 'registration_no', 'fuel_type_requested',
                     'price_per_liter', 'fprice', 'fuel_amount_requested', 'total_price', 'driver_name', 'current_mileage', 'region_code', 'fuel_station_name')

        widgets = {
            'price_per_liter': forms.Select(attrs={'onchange': 'PriceSelectedTextValue(this)',}),
            'fuel_amount_requested': forms.NumberInput(attrs={'oninput': 'reMultiply()',}),
            'total_price': forms.NumberInput(attrs={'readonly': 'true',}),
            'fprice': forms.NumberInput(attrs={'type':'hidden',}),
        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['price_per_liter'].widget.attrs.update()
        self.fields['fuel_amount_requested'].widget.attrs.update()
        self.fields['price_per_liter'].queryset = Fuel_price.objects.none()
        #Sself.fields['discount'].queryset = Fuel_price.objects.none()

        if 'fuel_type_requested' in self.data:
            try:
                fuel_name_id = int(self.data.get('fuel_type_requested'))
                self.fields['price_per_liter'].queryset = Fuel_price.objects.filter(fuel_name_id=fuel_name_id).order_by('fuel_price')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['price_per_liter'].queryset = self.instance.fuel_type_requested.price_per_liter_set.order_by('fuel_name')  

    def clean(self):
        cleaned_data = super().clean() 
        registration_no = cleaned_data.get('registration_no')
        price_per_liter = cleaned_data.get('price_per_liter')
        fuel_type_requested = cleaned_data.get('fuel_type_requested')
        price_per_liter = cleaned_data.get('price_per_liter')
        total = cleaned_data.get('total')

        yesterday = timezone.now() - timezone.timedelta(days=1)
        if Fuel_mgt.objects.filter(registration_no=registration_no, date_requested__gt=yesterday).exists():
            raise forms.ValidationError(f'This vehicle has an existing request raised today.')

        #Entry.objects.filter(~Q(date = 2006))
        #if total != price per liter * fuel amount requested
            #raise forms.ValidationError(f'seems there's an error in the total cost! kindly check again and submit')

class Fuel_mgt_issueForm(forms.ModelForm):

    class Meta:
        model = Fuel_mgt
        fields = ('fuel_station_name', 'liters_served', 'station_mileage')

        widgets = {
          #'price_per_liter': forms.Select(attrs={'onchange': 'PriceSelectedTextValue(this)',}),
            'fuel_amount_requested': forms.NumberInput(attrs={'oninput': 'reMultiply()',}),
            'amount': forms.NumberInput(attrs={'readonly': 'true',}),
            'fprice': forms.NumberInput(attrs={'type':'hidden',}),
        }


class Vehicle_issuesForm(forms.ModelForm):

    class Meta:
        model = Vehicle_issues
        fields = ('Vehicle_issue_topic', 'vehicle_registration_number', 'vehicle_issue')

class Work_assesmentsForm(forms.ModelForm):

    class Meta:
        model = Vehicle_issues
        fields = ('works_description', 'parts_required', 'works_total')

        widgets = {
            'works_total': forms.NumberInput(attrs={'placeholder': 'Enter cost estimates',}),
            'parts_required': forms.Textarea(attrs={'placeholder': 'Enter parts required!'}),
        }


class FormStepOne(forms.ModelForm):

    class Meta:
        model = Vehicle_handover
        fields = ('reason_for_handover', 'duty_station', 'registration_no', 'current_driver', 'assigned_driver')


class FormStepTwo(forms.ModelForm):

    class Meta:
        model = Vehicle_handover
        fields = ('head_lights', 'side_lights', 'rear_lights', 'mirrors_external', 'mirrors_internal', 'head_rests')

class FormStepThree(forms.ModelForm):

    class Meta:
        model = Vehicle_handover
        fields = ('wiper_arms', 'wiper_blades', 'sunvisors', 'radio', 'radio_knobs', 'speakers', 'radio_aerial', 'horn')

class FormStepFour(forms.ModelForm):

    class Meta:
        model = Vehicle_handover
        fields = ('spare_wheel', 'wheel_caps', 'wheel_spanner', 'floor_mats', 'tool_kit', 'jack', 'cigarette_lighter')

class FormStepFive(forms.ModelForm):

    class Meta:
        model = Vehicle_handover
        fields = ('vehicle_manual', 'life_savers', 'ignition_keys', 'door_keys', 'seat_belts', 'horn_relays', 'light_relays')

class FormStepSix(forms.ModelForm):

    class Meta:
        model = Vehicle_handover
        fields = ('head_rests', 'buffer_rubbers', 'petrol_tank_cap', 'key_holder', 'damage_on_departure', 'damage_on_arrival', 'cigarette_lighter')

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'birthdate', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

class Driver_IncidentsForm(forms.ModelForm):

    class Meta:
        model = Driver_Incidents
        fields = ('occurence_topic', 'driver_name', 'vehicle_assigned', 'station_assigned', 'details', 'action_taken')

class TestMForm(forms.ModelForm):

    class Meta:
        model = TestM
        fields = ('fuel_name', 'fuel_price', 'item_name', 'price', 'quantity', 'total')
        widgets = {
            'fuel_price': forms.Select(attrs={'onchange': 'reMultiply()',}),
            'quantity': forms.NumberInput(attrs={'oninput': 'reMultiply()',}),
            'total': forms.NumberInput(attrs={"readonly":"true"}),
        }

class Fuel_mgt_updatenewForm(forms.ModelForm):

    class Meta:
        model = Fuel_mgt_update
        fields = ('region', 'registration_no', 'fuel_type_requested',
                     'price_per_liter', 'fprice', 'fuel_amount_requested', 'total_price', 'driver_name', 'current_mileage', 'region_code')

        widgets = {
            'price_per_liter': forms.Select(attrs={'onchange': 'SelectedTextValue(this)',}),
            'fuel_amount_requested': forms.NumberInput(attrs={'onkeyup': 'reMultiply()',}),
            'total_price': forms.NumberInput(attrs={'readonly': 'true',}),
            'fprice': forms.NumberInput(attrs={'type':'hidden',}),
        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['price_per_liter'].widget.attrs.update()
        self.fields['fuel_amount_requested'].widget.attrs.update()
        

        self.fields['price_per_liter'].queryset = Fuel_price.objects.none()

        if 'fuel_type_requested' in self.data:
            try:
                fuel_name_id = int(self.data.get('fuel_type_requested'))
                self.fields['price_per_liter'].queryset = Fuel_price.objects.filter(fuel_name_id=fuel_name_id).order_by('fuel_price')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['price_per_liter'].queryset = self.instance.fuel_type_requested.price_per_liter_set.order_by('fuel_name')  

    def clean(self):
        cleaned_data = super().clean() 
        registration_no = cleaned_data.get('registration_no')
        price_per_liter = cleaned_data.get('price_per_liter')
        fuel_type_requested = cleaned_data.get('fuel_type_requested')
        price_per_liter = cleaned_data.get('price_per_liter')
        total = cleaned_data.get('total')

        yesterday = timezone.now() - timezone.timedelta(days=1)
        if Fuel_mgt.objects.filter(registration_no=registration_no, date_requested__gt=yesterday).exists():
            raise forms.ValidationError(f'This vehicle has an existing request raised today.')

class Fuel_mgt_xnForm(forms.ModelForm):

    class Meta:
        model = Fuel_mgt_xn
        fields = ('assign_request', 'region', 'work_ticket_number', 'registration_no', 'vendor', 'vendor_location', 'fuel_type_requested',
                     'price_per_liter', 'fprice', 'fuel_amount_requested', 'total_price', 'discount', 'current_mileage', 'driver_name', 'region_code')


        widgets = {
            'price_per_liter': forms.Select(attrs={'onchange': 'PriceSelectedTextValue(this)',}),
            'fuel_amount_requested': forms.NumberInput(attrs={'onkeyup': 'reMultiply()',}),
            'total_price': forms.NumberInput(attrs={'readonly': 'true',}),
            'fprice': forms.NumberInput(attrs={'type':'hidden',}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)       
        self.fields['vendor_location'].queryset = Vendor_station.objects.none()
        self.fields['fuel_type_requested'].queryset = Vendor_fuel_types.objects.none()
        self.fields['price_per_liter'].queryset = Fuel_price.objects.none()
        self.fields['discount'].queryset = Vendor_price.objects.none()

        if 'vendor' in self.data:
            try:
                vendor_name_id = int(self.data.get('vendor'))

                self.fields['vendor_location'].queryset = Vendor_station.objects.filter(vendor_name_id=vendor_name_id).order_by('vendor_location')
                self.fields['fuel_type_requested'].queryset = Vendor_fuel_types.objects.filter(vendor_name_id=vendor_name_id).order_by('vendor_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty child queryset
        elif self.instance.pk:
            self.fields['vendor_location'].queryset = self.instance.vendor.vendor_location.order_by('vendor')
            self.fields['fuel_type_requested'].queryset = self.instance.vendor.fuel_type_requested.order_by('vendor') 

        if 'fuel_type_requested' in self.data:
            try:
                fuel_name_id = int(self.data.get('fuel_type_requested'))

                self.fields['discount'].queryset = Vendor_price.objects.filter(fuel_name_id=fuel_name_id).order_by('fuel_name')
                self.fields['price_per_liter'].queryset = Vendor_price.objects.filter(fuel_name_id=fuel_name_id).order_by('fuel_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['price_per_liter'].queryset = self.instance.fuel_type_requested.price_per_liter_set.order_by('fuel_name')  
            self.fields['discount'].queryset = self.instance.fuel_type_requested.discount_set.order_by('fuel_name')  

    def clean(self):
        cleaned_data = super().clean() 
        registration_no = cleaned_data.get('registration_no')
        price_per_liter = cleaned_data.get('price_per_liter')
        fuel_type_requested = cleaned_data.get('fuel_type_requested')
        price_per_liter = cleaned_data.get('price_per_liter')
        total = cleaned_data.get('total')
        discount = cleaned_data.get('discount') 

        yesterday = timezone.now() - timezone.timedelta(days=1)
        if Fuel_mgt_xn.objects.filter(registration_no=registration_no, date_requested__gt=yesterday).exists():
            raise forms.ValidationError(f'This vehicle has an existing request raised today.')

        # if Vehicle_register.objects.filter(operational_status='grounded').values():
        #     raise forms.ValidationError(f'This vehicle is listed as grounded cannot be fueled, Kindly contact the fleet administrator for assistance')
        #Entry.objects.filter(~Q(date = 2006))
        #if total != price per liter * fuel amount requested
            #raise forms.ValidationError(f'seems there's an error in the total cost! kindly check again and submit')

class Fuel_mgt_xn_issueForm(forms.ModelForm):

    class Meta:
        model = Fuel_mgt_xn
        fields = ('vendor_location','fuel_amount_requested', 'liters_served', 'fuel_issue_complete')

    def __init__(self, *args, **kwargs):
        super(Fuel_mgt_xn_issueForm, self).__init__(*args, **kwargs)
        self.fields['fuel_amount_requested'].widget.attrs['readonly'] = True
    


        widgets = {
            'fuel_amount_requested': forms.NumberInput(attrs={'oninput': 'reMultiply()',}),
            'fprice': forms.NumberInput(attrs={'type':'hidden',}),
        }

    def clean(self):
        cleaned_data = super().clean() 
        liters_served = cleaned_data.get('liters_served')
        fuel_amount_requested = cleaned_data.get('fuel_amount_requested')


        if liters_served and fuel_amount_requested:
                # Only do something if both fields are valid so far.
               
                if liters_served > fuel_amount_requested:
                    raise forms.ValidationError(
                        "Attention!!\
                        You are serving more fuel than requested! Kindly review your order!"
                    )
                return cleaned_data

#messaging forms

class ThreadForm(forms.Form):
  username = forms.CharField(label='', max_length=100)
  
class MessageForm(forms.Form):
  message = forms.CharField(label='', max_length=1000)

#BPO appproval form
class BPOapproval_Form(forms.ModelForm):


    class Meta:
        model = Fuel_mgt_xn
        fields = ('BPO_approval', )

class Motorbike_registerForm(forms.ModelForm):
    class Meta:
        model = Motor_bike_register
        fields = ('motor_cycle_reg_no', 'make', 'model', 'region', 'fuel_type', 'engine_no', 'tank_capacity')

class Fuel_mgt_mbForm(forms.ModelForm):

    class Meta:
        model = Fuel_mgt_mb
        fields = ('assign_request', 'region', 'work_ticket_number', 'motor_cycle_reg_no', 'vendor', 'vendor_location', 'fuel_type_requested',
                     'price_per_liter', 'fprice', 'fuel_amount_requested', 'total_price', 'discount', 'current_mileage', 'rider_name', 'region_code')


        widgets = {
            'price_per_liter': forms.Select(attrs={'onchange': 'PriceSelectedTextValue(this)',}),
            'fuel_amount_requested': forms.NumberInput(attrs={'onkeyup': 'reMultiply()',}),
            'total_price': forms.NumberInput(attrs={'readonly': 'true',}),
            'fprice': forms.NumberInput(attrs={'type':'hidden',}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)       
        self.fields['vendor_location'].queryset = Vendor_station.objects.none()
        self.fields['fuel_type_requested'].queryset = Vendor_fuel_types.objects.none()
        self.fields['price_per_liter'].queryset = Fuel_price.objects.none()
        self.fields['discount'].queryset = Vendor_price.objects.none()

        if 'vendor' in self.data:
            try:
                vendor_name_id = int(self.data.get('vendor'))

                self.fields['vendor_location'].queryset = Vendor_station.objects.filter(vendor_name_id=vendor_name_id).order_by('vendor_location')
                self.fields['fuel_type_requested'].queryset = Vendor_fuel_types.objects.filter(vendor_name_id=vendor_name_id).order_by('vendor_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty child queryset
        elif self.instance.pk:
            self.fields['vendor_location'].queryset = self.instance.vendor.vendor_location.order_by('vendor')
            self.fields['fuel_type_requested'].queryset = self.instance.vendor.fuel_type_requested.order_by('vendor') 

        if 'fuel_type_requested' in self.data:
            try:
                fuel_name_id = int(self.data.get('fuel_type_requested'))

                self.fields['discount'].queryset = Vendor_price.objects.filter(fuel_name_id=fuel_name_id).order_by('fuel_name')
                self.fields['price_per_liter'].queryset = Vendor_price.objects.filter(fuel_name_id=fuel_name_id).order_by('fuel_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['price_per_liter'].queryset = self.instance.fuel_type_requested.price_per_liter_set.order_by('fuel_name')  
            self.fields['discount'].queryset = self.instance.fuel_type_requested.discount_set.order_by('fuel_name')  

    def clean(self):
        cleaned_data = super().clean() 
        registration_no = cleaned_data.get('registration_no')
        price_per_liter = cleaned_data.get('price_per_liter')
        fuel_type_requested = cleaned_data.get('fuel_type_requested')
        price_per_liter = cleaned_data.get('price_per_liter')
        total = cleaned_data.get('total')
        discount = cleaned_data.get('discount') 

        yesterday = timezone.now() - timezone.timedelta(days=1)
        if Fuel_mgt_xn.objects.filter(registration_no=registration_no, date_requested__gt=yesterday).exists():
            raise forms.ValidationError(f'This vehicle has an existing request raised today.')

        #Entry.objects.filter(~Q(date = 2006))
        #if total != price per liter * fuel amount requested
            #raise forms.ValidationError(f'seems there's an error in the total cost! kindly check again and submit')
