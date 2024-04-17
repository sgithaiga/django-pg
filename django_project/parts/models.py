from django.conf import settings
from django.db import models, IntegrityError
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from transport.models import Vehicle_register, UserUnit, station
from django.utils.crypto import get_random_string
from django.utils import timezone
from transport.models import Vehicle_issues, Driver
# Create your models here.
class Vehicle(models.Model):

    registration_number = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True)
    date_ordered = models.DateTimeField(default=timezone.now)
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    order = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('parts:vehicle_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.registration_number.registration_no

class Parts(models.Model):
    YES = 'Yes'
    NO = 'No'    
    FITTED = 'Fitted'
    NOT_FITTED = 'Not Fitted'
    
    DELIVERY_STATUS = [
        (YES, ('Yes')),
        (NO, ('No')),
    ]
   
    FITMENT_STATUS = [
        (FITTED, ('Fitted')),
        (NOT_FITTED, ('Not Fitted')),
    ]
    
    part_name = models.CharField(null=False, blank=False, max_length=255)
    registration_number = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True)
    # registration_number = models.ForeignKey('Vehicle_register', null=False, blank=False, on_delete=models.CASCADE, related_name='reg_no')
    quantity = models.CharField(null=True, blank=False, max_length=255)
    delivered = models.CharField(max_length=100, choices=DELIVERY_STATUS)
    date_delivered = models.DateField(blank=True, null=True)
    fitted = models.CharField(max_length=100, choices=FITMENT_STATUS)
    date_fitted = models.DateField(blank=True, null=True)
    serial_number = models.CharField(null=True, blank=True, max_length=255)
    
    def __str__(self):
        return self.part_name
    
    def get_absolute_url(self):
        # returns  to the vehicle list 
        return reverse('list-parts')


#remove these two models    
class Tire(models.Model):
    brand_name = models.CharField(null=True, blank=True, max_length=255)
    tire_serial_number = models.IntegerField()
    tire_details = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return self.brand_name  
class Tire_Installation(models.Model):
    pass

#use this for tyre management
class TyreIssuance(models.Model):
    MITCHELLIN = 'Mitchellin'
    GOODYEAR = 'Goodyear'    
    YANA = 'Yana'
    PIRELLI = 'Pirelli'
    
    TYRE_MAKE = [
        (MITCHELLIN, ('Mitchellin')),
        (GOODYEAR, ('Goodyear')),
        (YANA, ('Yana')),
        (PIRELLI, ('Pirelli')),
    ]    
    vehicle = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE)
    issued_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tyre_issues')
    region = models.ForeignKey(UserUnit, on_delete=models.SET_NULL, null=True)  # Assuming you have a Region model
    unique_number = models.CharField(max_length=255, editable=False, unique=True)
    date_issued = models.DateTimeField(default=timezone.now)
    size = models.CharField(null=True, blank=True, max_length=255)
    received_by = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, related_name='tyre_receiver')
    make = models.CharField(max_length=100, choices=TYRE_MAKE, null=True)
    
    
    def save(self, *args, **kwargs):
        if not self.unique_number:
            # Generate a unique number in the format: registration_no/region/unique_number
            while True:
                unique_number = get_random_string(length=5).upper()  # Generate a random string of length 5
                self.unique_number = f"{self.vehicle.registration_no}/{self.region}/{unique_number}"
                try:
                    super().save(*args, **kwargs)
                except IntegrityError:
                    continue
                else:
                    break
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.unique_number

class AutoGarage(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class VehicleDispatch(models.Model):
    
    LOCAL = 'Local'
    EXTERNAL = 'External'        
    
    DISPATCH_LOCATION = [
        (LOCAL, ('Local')),
        (EXTERNAL, ('External')),
    ]
    registration_no = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, related_name='dispatch')
    auto_garage = models.CharField(max_length=100, choices=DISPATCH_LOCATION)
    garage_name = models.ForeignKey(AutoGarage, on_delete=models.CASCADE, related_name='garage_name', null=True)
    date_dispatched = models.DateField(null=True)
    date_vehicle_received = models.DateField(null=True)
    authorization_memo = models.FileField(upload_to='documents/', null=True)
    service_invoice = models.FileField(upload_to='documents/', null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'dispatchuser', null=True )
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'dispatchuserupdate', null=True )
    
    def __str__(self):
        return self.registration_no.registration_no
    
    # def get_absolute_url(self):
    #     # returns us to the list view. can also set this to app-home
    #     return reverse('fuel-mgtm-list')
    
class VehicleAssessment(models.Model):
    registration_no = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, related_name='assessment', null=True)
    works_done = models.TextField(null=True)
    works_total = models.FloatField(null=True)
    repairs_verified = models.BooleanField(null=True)
    repairs_verified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='repairs_verifier', null=True)
    date_verified = models.DateField(auto_now=True)
    repairs_approved = models.BooleanField(null=True)
    repairs_approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='repairs_approver', null=True)
    date_approved = models.DateField(null=True)

    def __str__(self):
        return self.registration_no.registration_no
    
class ImprestPartsAquisition(models.Model):
    
    ELECTRICAL = 'Electrical'
    SUSPENSION = 'Suspension' 
    TRANSMISSION = 'Transmission'
    TYRE = 'Tyre'
    WINDSCREEN = 'Windscreen'
    SERVICE_PART = 'Service part'  
    
    PART_CATEGORY = [
        (ELECTRICAL, ('Electrical')),
        (SUSPENSION, ('Suspension')),
        (TRANSMISSION, ('Transmission')),
        (TYRE, ('Tyre')),
        (WINDSCREEN, ('Windscreen')),
        (SERVICE_PART, ('Service part')),
    ]    
    
    part_category = models.CharField(max_length=100, choices=PART_CATEGORY)
    part_name = models.CharField(max_length=100)
    part_cost = models.FloatField(null=True)
    registration_no = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, related_name='partsimprest')
    station = models.ForeignKey(station, on_delete=models.CASCADE, related_name='stationimprest')
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userimprest', null=True)
    date_requested = models.DateField(auto_now_add=True)
    approve_requisition = models.BooleanField(default=False)
    date_approved = models.DateField(auto_now=True, null=True, blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approverimprest', null=True)
    invoice = models.FileField(upload_to='imprest/invoices/', blank=False, null=True)
    invoice_no = models.CharField(max_length=255, unique=True, null=True)
    vendor=models.CharField(max_length=255, null=True)
    quantity = models.FloatField(null=True)
    total = models.FloatField(null=True)
    
    def calculate_total(self):
        if self.part_cost and self.quantity:
            self.total = self.part_cost * self.quantity

    def save(self, *args, **kwargs):
        self.calculate_total()
        if self.pk:  # Check if the object already exists (i.e., it's an update)
            self.date_requested = timezone.now()
            
        super().save(*args, **kwargs)
        
    def __str__(self):
            return f"Part: {self.part_name}, Category: {self.part_category}, Cost: {self.total}, Registration No: {self.registration_no}"