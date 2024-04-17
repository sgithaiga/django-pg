from pickle import TRUE
from pyexpat import model
from django.conf import settings
from django.db.models import ExpressionWrapper
from django.db import models
import uuid
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image





# Create your models here.
class station (models.Model):

    HEADQUARTERS = 'Headquarters'
    EASTERN_REGION = 'Eastern Region'
    CENTRAL_REGION = 'Central Region'    
    NORTHERN_REGION = 'Northern Region'
    NORTH_EASTERN = 'North Eastern'
    SOUTHERN_REGION = 'Southern Region'
    WESTERN_REGION = 'Western Region'
    INFORMAL_SETTLEMENT_REGION = 'Informal Settlements Region'
    RUAI = 'Ruai'
    GIGIRI = 'Gigiri'
    KABETE_LABORATORY = 'Kabete Laboratory'
    KABETE_TREATMENT_WORKS = 'Kabete Treatment Works'
    RUIRU_DAM = 'Ruiru Dam'
    NGETHU_TREATMENT_WORKS = 'Ngethu Treatment Works'
    THIKA_DAM = 'Thika Dam'
    SASUMUA_TREATMENT_WORKS = 'Sasumua Treatment Works'
    KARIOBANGI_TREATMENT_WORKS = 'Kariobangi Treatment Works'

    REGIONS = [
        (HEADQUARTERS, ('Headquarters')),
        (EASTERN_REGION, ('Eastern Region')),
        (CENTRAL_REGION, ('Central Region')),
        (NORTHERN_REGION, ('Northern Region')),
        (NORTH_EASTERN, ('North Eastern')),
        (SOUTHERN_REGION, ('Southern Region')),
        (WESTERN_REGION, ('Western Region')),
        (INFORMAL_SETTLEMENT_REGION, ('Informal Settlements Region')),
        (RUAI, ('Ruai')),
        (RUIRU_DAM, ('Ruiru Dam')),
        (GIGIRI, ('Gigiri')),
        (KABETE_LABORATORY, ('Kabete Laboratory')),
        (NGETHU_TREATMENT_WORKS, ('Ngethu Treatment Works')),
        (THIKA_DAM, ('Thika Dam')),
        (SASUMUA_TREATMENT_WORKS, ('Sasumua Treatment Works')),
        (KARIOBANGI_TREATMENT_WORKS, ('Kariobangi Treatment Works')),
    ]

    station = models.CharField(
        max_length=200,
        choices=REGIONS,
        default=EASTERN_REGION,
        unique=True,
    )  

    def __str__(self):
        return self.station 

class Fuel_name (models.Model):
    fuel_name = models.CharField(max_length=200, null = True) 

    def __str__(self):
        return self.fuel_name

class Fuel_price (models.Model):
    fuel_name = models.ForeignKey(Fuel_name, on_delete=models.CASCADE, null=True) 
    fuel_price = models.FloatField(blank=True, null=True) 
    date_entered = models.DateTimeField(auto_now=True, null=True)
    discount_price = models.FloatField(blank=True, null=True) 

    
    def __str__(self):
        return self.fuel_name.fuel_name

class Fuel_station (models.Model):
    fuel_station_name = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.fuel_station_name

class Make (models.Model):
    ISUZU = 'Isuzu'
    MITSUBISHI = 'Mitsubishi'
    NISSAN = 'Nissan'
    CASE = 'Case'
    TOYOTA_HILUX = 'Toyota Hilux'
    TOYOTA_LAND_CRUISER = 'Toyota Land Cruiser'
    TOYOTA = 'Toyota'
    MERCEDES_BENZ = 'Mercedes Benz'
    MAN = 'Man'
    IVECO = 'Iveco'
    NEW_HOLLLAND = 'New Holland'
    FIAT = 'Fiat'
    JCB = 'JCB'


    VEHICLE_MAKE = [
        (ISUZU, ('Isuzu')),
        (MITSUBISHI, ('Mitsubishi')),
        (NISSAN, ('Nissan')),
        (CASE, ('Case')),
        (TOYOTA, ('Toyota')),
        (MERCEDES_BENZ, ('Mercedes Benz')),
        (MAN, ('Man')),
        (IVECO, ('Iveco')),
        (FIAT, ('Fiat')),
        (IVECO, ('Iveco')),
        (JCB, ('New JCB')),
    ]





    vehicle_name = models.CharField(
        max_length=200,
        choices=VEHICLE_MAKE,
        default=ISUZU,
        unique=True
    )
    def __str__(self):
        return self.vehicle_name

class Model (models.Model):
    model_name = models.ForeignKey(Make, on_delete=models.CASCADE, null=True) 
    vehicle_model = models.CharField(max_length=200, null = True) 

    def __str__(self):
        return self.vehicle_model

class Vehicle_register (models.Model):

    NA = 'not applicable'
    OPERATIONAL = 'operational'
    GROUNDED = 'grounded'
    SERVICABLE = 'servicable'
    ACCIDENT = 'accident'
    ACCIDENT_WRITE_OFF = 'write off'
    INSURANCE = 'insurance'
    ECONOMICAL_TO_REPAIR = 'reparable'
    UN_ECONOMICAL_TO_REPAIR = 'not reparable'
    REPAIRS = 'Repairs in progress'
    HEADQUARTERS = 'Headquarters'
    EASTERN_REGION = 'Eastern Region'
    CENTRAL_REGION = 'Central Region'    
    NORTHERN_REGION = 'Northern Region'
    NORTH_EASTERN = 'North Eastern'
    SOUTHERN_REGION = 'Southern Region'
    WESTERN_REGION = 'Western Region'
    INFORMAL_SETTLEMENT_REGION = 'Informal Settlements Region'
    RUAI = 'Ruai'
    GIGIRI = 'Gigiri'
    KABETE_LABORATORY = 'Kabete Laboratory'
    KABETE_TREATMENT_WORKS = 'Kabete Treatment Works'
    RUIRU_DAM = 'Ruiru Dam'
    NGETHU_TREATMENT_WORKS = 'Ngethu Treatment Works'
    THIKA_DAM = 'Thika Dam'
    SASUMUA_TREATMENT_WORKS = 'Sasumua Treatment Works'
    KARIOBANGI_TREATMENT_WORKS = 'Kariobangi Treatment Works'
    MANUAL_TRANS = 'Manual Transmission'
    AUTO_TRANS = 'Automatic Transmission'
    REAR_WHEEL_DRIVE = 'Rear Wheel Drive'
    FOUR_WHEEL_DRIVE = 'Four Wheel Drive'
    DOUBLE_CAB = 'Double Cab'
    TIPPER = 'Tipper'
    TANKER = 'Tanker'
    FLUSHING_UNIT = 'Flushing unit'
    EXHAUSTER = 'Exhauster'
    LOW_LOADER = 'Low Loader'
    SALOON = 'Saloon'
    EXCAVATOR = 'Excavator'
    SUV = 'SUV'
    MOTOR_BIKE = 'motor Bike'
    PICKUP = 'Pick up'
    LORRY = 'Lorry'
    BACKHOE_LOADER = 'Backhoe Loader'
    STATION_WAGON = 'Station Wagon'
    VAN = 'Van'
    SPECIAL_PURPOSE = 'Special Purpose'
    PRIME_MOVER = 'Prime Mover'
    TRACTOR = 'Tractor'
    L_SIDED = 'L_Sided'
    WHITE = 'White'
    WHITE_CREAM = 'White_cream'
    WHITE_BLUE = 'White_blue'
    WHITE_GREEN = 'White_green'
    GREY_METALLIC = 'Metallic grey'
    BLUE = 'Blue'
    SILVER = 'Silver'
    DARK_STEEL = 'Dark steel'
    YELLOW = 'Yellow'
    GREY_BLUE = 'Grey blue'
    GOLD = 'Gold'
    GREEN = 'Green'
    COMMERCIAL_GOODS = 'Commercial goods'
    PRIVATE = 'Private'
    HEADQUARTERS_NRW = 'Headquarters NRW'


    


    REGIONS = [
        (HEADQUARTERS, ('Headquarters')),
        (EASTERN_REGION, ('Eastern Region')),
        (CENTRAL_REGION, ('Central Region')),
        (NORTHERN_REGION, ('Northern Region')),
        (NORTH_EASTERN, ('North Eastern')),
        (SOUTHERN_REGION, ('Southern Region')),
        (WESTERN_REGION, ('Western Region')),
        (INFORMAL_SETTLEMENT_REGION, ('Informal Settlements Region')),
        (RUAI, ('Ruiru Dam')),
        (GIGIRI, ('Gigiri')),
        (KABETE_LABORATORY, ('Kabete Laboratory')),
        (RUIRU_DAM, ('Ruiru Dam')),
        (NGETHU_TREATMENT_WORKS, ('Ngethu Treatment Works')),
        (THIKA_DAM, ('Thika Dam')),
        (SASUMUA_TREATMENT_WORKS, ('Sasumua Treatment Works')),
        (KARIOBANGI_TREATMENT_WORKS, ('Kariobangi Treatment Works')),
        (HEADQUARTERS_NRW, ('Headquarters NRW')),
    ]
    
    OPERATIONAL_STATUS = [
        (OPERATIONAL, ('Operational')),
        (GROUNDED, ('Grounded')),
        (NA, ('Not Applicable')),
        
    ]
    MECHANICAL_STATUS = [
        (ACCIDENT, ('Accident')),
        (ACCIDENT_WRITE_OFF, ('Accident(Write off)')),
        (SERVICABLE, ('Servicable')),
        (INSURANCE, ('Insurance')),
        (ECONOMICAL_TO_REPAIR, ('Reparable')),
        (UN_ECONOMICAL_TO_REPAIR, ('Not Reparable')),
        (REPAIRS, ('Repairs in progress')),
        (NA, ('Not Applicable')),
    ]
    TRANSMISSION = [
        (MANUAL_TRANS, ('Manual Transmission')),
        (AUTO_TRANS, ('Automatical Transmission')),

    ]

    POWERTRAIN = [
        (REAR_WHEEL_DRIVE, ('Rear Wheel Drive')),
        (FOUR_WHEEL_DRIVE, ('Four Wheel Drive')),
    ]

    BODY_TYPES = [
        (DOUBLE_CAB, ('Double Cab')),
        (TIPPER, ('Tipper')),    
        (TANKER, ('Tanker')),
        (LOW_LOADER, ('Low Loader')),
        (SALOON, ('Saloon')),
        (EXCAVATOR, ('Excavator')),
        (SUV, ('SUV')),
        (MOTOR_BIKE, ('Motor Bike')),
        (PICKUP, ('Pickup')),
        (LORRY, ('Lorry')),
        (BACKHOE_LOADER, ('Backhoe loader')),
        (STATION_WAGON, ('Station wagon')),
        (VAN, ('Van')),
        (SPECIAL_PURPOSE, ('Special purpose')),
        (PRIME_MOVER, ('Prime mover')),
        (TRACTOR, ('Tractor')),
        (L_SIDED, ('L_sided')),


    ]

    COLORS = [
        (WHITE, ('White')),
        (WHITE_BLUE, ('White blue')),
        (WHITE_CREAM, ('White cream')),
        (WHITE_GREEN, ('White green')),
        (GREY_METALLIC, ('Grey metallic')),
        (BLUE, ('Blue')),
        (SILVER, ('Silver')),
        (DARK_STEEL, ('Dark steel')),
        (YELLOW, ('Yellow')),
        (GREEN, ('Green')),
        (GREY_BLUE, ('Grey blue')),
        (GOLD, ('Gold')),
        (GREEN, ('Green')),
        (GREY_BLUE, ('Grey blue')),

    ]

    TAX_CLASS = [
        (COMMERCIAL_GOODS, ('Commercial goods')),
        (PRIVATE, ('Private')),
    ]

    PLANTS_MACHINERY = [
        (TANKER, ('Tanker')),
        (EXCAVATOR, ('Excavator')),        
        (EXHAUSTER, ('Exhauster')),
        (FLUSHING_UNIT, ('Flushing Unit')),
    ] 
    registration_no = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(station, on_delete=models.CASCADE, null=True)
    make = models.ForeignKey(Make, on_delete=models.CASCADE, null=True)
    engine_capacity = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True)
    drive_type = models.CharField(max_length=100, choices=POWERTRAIN, default=REAR_WHEEL_DRIVE,)
    transmission =  models.CharField(
        max_length=200,
        choices=TRANSMISSION,
        default=MANUAL_TRANS,
    )
    body_type = models.CharField(max_length=100, choices=BODY_TYPES,)
    fuel_tank_capacity = models.CharField(max_length=100)
    operational_status = models.CharField(
        max_length=200,
        choices=OPERATIONAL_STATUS,
        default=NA,
    )
    mechanical_status = models.CharField(
        max_length=200,
        choices=MECHANICAL_STATUS,
        default=ACCIDENT,
    )
    remarks= models.TextField(blank = True)
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    date_registered = models.DateTimeField(default=timezone.now)
    log_book = models.FileField(upload_to='documents/', null=True)
    chassis_number = models.CharField(max_length=100,blank=True, null=True, unique=True)
    manufacture_year = models.DateField(blank=True, null=True)
    engine_no = models.CharField(max_length=100, unique=True, null=True)
    color = models.CharField(max_length=50, choices=COLORS, default=WHITE)
    vehicle_registration_date = models.DateField(blank=True, null=True)
    gross_weight = models.IntegerField(blank=True, null=True)
    tare_weight = models.IntegerField(blank=True, null=True)
    passengers = models.IntegerField(blank=True, null=True)
    tax_class = models.CharField(max_length=50, choices=TAX_CLASS, default = NA)
    axles = models.IntegerField(blank=True, null=True)
    load_capacity = models.IntegerField(blank=True, null=True)
    log_book_number = models.CharField(max_length=100, null=True)
    type =  models.CharField(max_length=100, choices=PLANTS_MACHINERY, null=True)
    fuel_type = models.ForeignKey(Fuel_name, on_delete=models.CASCADE, null=True )


    def __str__(self):
        return self.registration_no

    def get_absolute_url(self):
        # returns  to the vehicle list 
        return reverse('vehicle-list')

class Driver (models.Model):

    HEADQUARTERS = 'Headquarters'
    EASTERN_REGION = 'Eastern Region'
    CENTRAL_REGION = 'Central Region'    
    NORTHERN_REGION = 'Northern Region'
    NORTH_EASTERN = 'North Eastern'
    SOUTHERN_REGION = 'Southern Region'
    WESTERN_REGION = 'Western Region'
    INFORMAL_SETTLEMENT_REGION = 'Informal Settlements Region'
    RUAI = 'Ruai'
    GIGIRI = 'Gigiri'
    KABETE_LABORATORY = 'Kabete Laboratory'
    KABETE_TREATMENT_WORKS = 'Kabete Treatment Works'
    RUIRU_DAM = 'Ruiru Dam'
    NGETHU_TREATMENT_WORKS = 'Ngethu Treatment Works'
    THIKA_DAM = 'Thika Dam'
    SASUMUA_TREATMENT_WORKS = 'Sasumua Treatment Works'
    KARIOBANGI_TREATMENT_WORKS = 'Kariobangi Treatment Works'
    MALE = 'Male'
    FEMALE = 'Female'
    DRIVER = 'Driver'
    PLANT_OPERATOR = 'Plant operator'

    REGIONS = [
        (HEADQUARTERS, ('Headquarters')),
        (EASTERN_REGION, ('Eastern Region')),
        (CENTRAL_REGION, ('Central Region')),
        (NORTHERN_REGION, ('Northern Region')),
        (NORTH_EASTERN, ('North Eastern')),
        (SOUTHERN_REGION, ('Southern Region')),
        (WESTERN_REGION, ('Western Region')),
        (INFORMAL_SETTLEMENT_REGION, ('Informal Settlements Region')),
        (RUAI, ('Ruiru Dam')),
        (GIGIRI, ('Gigiri')),
        (KABETE_LABORATORY, ('Kabete Laboratory')),
        (RUIRU_DAM, ('Ruiru Dam')),
        (NGETHU_TREATMENT_WORKS, ('Ngethu Treatment Works')),
        (THIKA_DAM, ('Thika Dam')),
        (SASUMUA_TREATMENT_WORKS, ('Sasumua Treatment Works')),
        (KARIOBANGI_TREATMENT_WORKS, ('Kariobangi Treatment Works')),
    ]

    GENDER = [
        (MALE, ('Male')),
        (FEMALE, ('Female')),
    ]
    JOB_TITLE = [
        (DRIVER, ('Driver')),
        (PLANT_OPERATOR, ('Plant operator')),
    ]

    full_name = models.CharField(max_length=100, unique=True)
    pf_no = models.CharField(max_length=100, unique=True )
    gender = models.CharField(max_length=100, choices=GENDER)
    region_assigned = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    license_number = models.CharField(max_length=100, unique=True)
    expiry_date = models.DateField(blank=True, null=True)
    driver_history = models.TextField()
    assigned_vehicle = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True)
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    job_title = models.CharField(max_length=100, choices=JOB_TITLE, null=True)

    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        # returns  to the vehicle list 
        return reverse('driver-list')


class Request_fuel (models.Model):

    HEADQUARTERS = 'Headquarters'
    EASTERN_REGION = 'Eastern Region'
    CENTRAL_REGION = 'Central Region'    
    NORTHERN_REGION = 'Northern Region'
    NORTH_EASTERN = 'North Eastern'
    SOUTHERN_REGION = 'Southern Region'
    WESTERN_REGION = 'Western Region'
    INFORMAL_SETTLEMENT_REGION = 'Informal Settlements Region'
    RUAI = 'Ruai'
    GIGIRI = 'Gigiri'
    KABETE_LABORATORY = 'Kabete Laboratory'
    KABETE_TREATMENT_WORKS = 'Kabete Treatment Works'
    RUIRU_DAM = 'Ruiru Dam'
    NGETHU_TREATMENT_WORKS = 'Ngethu Treatment Works'
    THIKA_DAM = 'Thika Dam'
    SASUMUA_TREATMENT_WORKS = 'Sasumua Treatment Works'
    KARIOBANGI_TREATMENT_WORKS = 'Kariobangi Treatment Works'
    DIESEL = 'Diesel'
    PETROL = 'Petrol'
    LUBRICANT = 'Lubricant'

    REGIONS = [
        (HEADQUARTERS, ('Headquarters')),
        (EASTERN_REGION, ('Eastern Region')),
        (CENTRAL_REGION, ('Central Region')),
        (NORTHERN_REGION, ('Northern Region')),
        (NORTH_EASTERN, ('North Eastern')),
        (SOUTHERN_REGION, ('Southern Region')),
        (WESTERN_REGION, ('Western Region')),
        (INFORMAL_SETTLEMENT_REGION, ('Informal Settlements Region')),
        (RUAI, ('Ruai')),
        (GIGIRI, ('Gigiri')),
        (KABETE_LABORATORY, ('Kabete Laboratory')),
        (RUIRU_DAM, ('Ruiru Dam')),
        (NGETHU_TREATMENT_WORKS, ('Ngethu Treatment Works')),
        (THIKA_DAM, ('Thika Dam')),
        (SASUMUA_TREATMENT_WORKS, ('Sasumua Treatment Works')),
        (KARIOBANGI_TREATMENT_WORKS, ('Kariobangi Treatment Works')),
    ]

    FUEL_TYPE = [
        (DIESEL, ('Diesel')),
        (PETROL, ('Petrol')),
        (LUBRICANT, ('Lubricant')),
    ]
    fuel_request_reference = models.UUIDField(default=uuid.uuid4)
    vehicle_registration_number = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True, related_name='+')
    region = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    fuel_type_requested = models.ForeignKey(Fuel_name, on_delete=models.CASCADE, null = True)
    fuel_amount_requested = models.DecimalField(max_digits=8, decimal_places=2)
    price_per_liter = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'approver', null=True)
    date_approved = models.DateTimeField(auto_now=True, null=True)
    closed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'fueler',  null=True)
    fuel_issue_complete = models.BooleanField(default=False)
    date_closed = models.DateTimeField(null=True)
    declined = models.BooleanField(default=False)
    reason = models.TextField(blank = True, null=True)
    barcode = models.ImageField(upload_to='images/', null=True, blank=True)
    driver_assigned = models.ForeignKey(Driver, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.region

    def get_absolute_url(self):
        # returns us to the list view. can also set this to app-home
        return reverse('request-fuel-list')

class Assign_fuel (models.Model):

    DEVANI_LTD = 'Devani Ltd along Kitui road'
    SHELL = 'Shell Filling station along Lusaka road'
    DIESEL = 'Diesel'
    PETROL = 'Petrol'
    LUBRICANT = 'Lubricant'

    FUEL_STATIONS = [
        (DEVANI_LTD, ('Devani Ltd - Kitui Rd')),
        (SHELL, ('Shell Station - Lusaka Rd')),    
    ]

    FUEL_TYPE = [
        (DIESEL, ('Diesel')),
        (PETROL, ('Petrol')),
        (LUBRICANT, ('Lubricant')),    
    ]

    station_name = models.CharField(
        max_length=200,
        choices=FUEL_STATIONS,
        default=DEVANI_LTD,
    )
    fuel_type = models.CharField(
        max_length=200,
        choices=FUEL_TYPE,
        default=DIESEL,
    )
    driver_name = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    previous_liters_served = models.CharField(max_length=100) 
    price_per_liter = models.DecimalField(max_digits=8, decimal_places=2)
    liters_served = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.DecimalField(max_digits=8, decimal_places=2)    
    vehicle = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null=True)
    previous_mileage = models.CharField(max_length=100)
    current_mileage = models.CharField(max_length=100)
    distance_covered = models.CharField(max_length=100, null=True)
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    station = models.ForeignKey(station, on_delete=models.CASCADE, null=True)


    def publish(self):
        self.date_posted = timezone.now()
        self.save()
    
    def __str__(self):
        return self.station_name

    def get_absolute_url(self):
        # returns us to the post-detail view. can also set this to blog-home
        return reverse('fuel-list')


class UserUnit(models.Model):

    name = models.CharField(max_length=100, unique=True)
    region_name = models.ForeignKey(station, on_delete=models.CASCADE, related_name = 'rname', null = True)

    def __str__(self):
        return self.name

class Fuel_mgt (models.Model):

    request_reference = models.UUIDField(default=uuid.uuid4)
    region = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    registration_no = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True, related_name='+')
    fuel_type_requested = models.ForeignKey(Fuel_name, on_delete=models.CASCADE, null = True)
    fuel_amount_requested = models.DecimalField(max_digits=8, decimal_places=2)
    price_per_liter = models.ForeignKey(Fuel_price, on_delete=models.CASCADE, null = True)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'requester1', null=True)
    date_requested = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'approver1', null=True)
    date_approved = models.DateTimeField(auto_now=True, null=True)
    closed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'fueler1',  null=True)
    fuel_issue_complete = models.BooleanField(default=False)
    date_closed = models.DateTimeField(default=timezone.now)
    declined = models.BooleanField(default=False)
    reason = models.TextField(blank = True, null=True)
    barcode = models.ImageField(upload_to='images/', null=True, blank=True)
    fuel_station_name = models.ForeignKey(Fuel_station, on_delete=models.CASCADE, null = True)
    driver_name = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    previous_liters_served = models.CharField(max_length=100, null=True) 
    liters_served = models.IntegerField(null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)    
    previous_mileage = models.CharField(max_length=100, null=True, blank=True)
    current_mileage = models.CharField(max_length=100, null=True, blank=True)
    distance_covered = models.CharField(max_length=100, null=True)
    attended_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'attendant', null=True)
    date_fueled = models.DateTimeField(default=timezone.now)
    region_code = models.ForeignKey(UserUnit, on_delete=models.CASCADE, related_name = 'rcode', null=True)
    station_mileage = models.CharField(max_length=100, null=True, blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    fprice =  models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return self.registration_no.registration_no

    def get_fuel_issued_price(self):
        
        if self.liters_served is not None:    
        
            #create variable tprice to store value and return true if condition is met
            #return 0 as a safe fall back if false
            tprice = self.liters_served * self.price_per_liter.fuel_price

            return tprice
        return 0

    def get_absolute_url(self):
        # returns us to the list view. can also set this to app-home
        return reverse('fuel-mgt-list')

    #def get_total_fuel_cost(self):
        # return fuel cost
        #return self.fuel_amount_requested * self.Fuel_price.price_per_liter
    
    #def save(self, *args, **kwargs):
        ##self.total_price = self.fuel_amount_requested * self.price_per_liter.fuel_price
        #super(Fuel_mgt, self).save(*args, **kwargs)




class Mechanic_reg(models.Model):
    mechanic_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'mech', null=True)
    pf_no = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.pf_no

class Vehicle_issues (models.Model):

    issue_reference = models.UUIDField(default=uuid.uuid4)
    Vehicle_issue_topic = models.CharField(max_length=100, null=True)
    vehicle_registration_number = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True)
    vehicle_issue =  models.TextField(blank = True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'logger', null=True)
    date_created = models.DateTimeField(default=timezone.now)
    driver_assigned = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name = 'driverassigned', null = True)
    region = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    mechanic = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'mechassigned', null=True)
    vehicle_in = models.BooleanField(default=False)
    declined = models.BooleanField(default=False)
    reason_for_decline = models.TextField(blank = True, null=True)
    current_mileage = models.CharField(max_length=100, null=True)
    next_service = models.CharField(max_length=100, null=True)
    date_received = models.DateTimeField(default=timezone.now)
    service = models.BooleanField(default=False)
    works_description = models.TextField(blank = True, null=True)
    service_total = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    repair = models.BooleanField(default=False)
    repair_description = models.TextField(blank = True, null=True)
    works_total = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    parts_requisition_date = models.DateTimeField(default=timezone.now)
    parts_received_date = models.DateTimeField(default=timezone.now)
    further_works_required_remarks = models.TextField(blank = True, null=True)
    vehicle_out = models.BooleanField(default=False)
    date_released = models.DateTimeField(default=timezone.now)
    down_time = models.CharField(max_length=100, null=True)
    transport_assistant = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'ta', null=True)
    transport_supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'ts', null=True)
    transport_officer = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'to', null=True)
    mechanic_assesment = models.TextField(blank = True, null=True)
    approve_works = models.BooleanField(default=False)
    check_report = models.BooleanField(default=False)
    parts_required = models.TextField(blank = True, null=True)

    def __str__(self):
        return self.Vehicle_issue_topic

    def get_absolute_url(self):
        # returns  to the vehicle list 
        return reverse('v-issue-list')
    





class Vehicle_handover (models.Model):
    reason_for_handover = models.CharField(max_length=200, null=True)
    duty_station = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    registration_no = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True)
    head_lights = models.CharField(max_length=100, null=True)
    side_lights = models.CharField(max_length=100, null=True)
    rear_lights = models.CharField(max_length=100, null=True)
    mirrors_external = models.CharField(max_length=100, null=True)
    mirrors_internal = models.CharField(max_length=100, null=True)
    wiper_arms = models.CharField(max_length=100, null=True)
    wiper_blades = models.CharField(max_length=100, null=True)
    sunvisors = models.CharField(max_length=100, null=True)
    radio = models.CharField(max_length=100, null=True)
    radio_knobs = models.CharField(max_length=100, null=True)
    speakers = models.CharField(max_length=100, null=True)
    radio_aerial = models.CharField(max_length=100, null=True)
    horn = models.CharField(max_length=100, null=True)
    spare_wheel = models.CharField(max_length=100, null=True)
    wheel_caps = models.CharField(max_length=100, null=True)
    wheel_spanner = models.CharField(max_length=100, null=True)
    floor_mats = models.CharField(max_length=100, null=True)
    tool_kit = models.CharField(max_length=100, null=True)
    jack = models.CharField(max_length=100, null=True)
    cigarette_lighter = models.CharField(max_length=100, null=True)
    vehicle_manual = models.CharField(max_length=100, null=True)
    life_savers = models.CharField(max_length=100, null=True)
    ignition_keys = models.CharField(max_length=100, null=True)
    door_keys = models.CharField(max_length=100, null=True)
    seat_belts = models.CharField(max_length=100, null=True)
    horn_relays = models.CharField(max_length=100, null=True)
    light_relays = models.CharField(max_length=100, null=True)
    head_rests = models.CharField(max_length=100, null=True)
    buffer_rubbers = models.CharField(max_length=100, null=True)
    petrol_tank_cap = models.CharField(max_length=100, null=True)
    key_holder = models.CharField(max_length=100, null=True)
    damage_on_departure =  models.TextField(blank = True, null=True)
    damage_on_arrival = models.TextField(blank = True, null=True)
    current_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name = 'currdriver', null=True)
    assigned_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name = 'issueddriver', null=True)
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'vhandover', null=True)
    date_issued = models.DateTimeField(default=timezone.now)
    received_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'vreceived', null=True)
    date_received = models.DateTimeField(default=timezone.now)
    authorised_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'vauthorised', null=True)
    date_authorised = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reason_for_handover

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Driver_Incidents(models.Model):
    occurence_topic = models.CharField(max_length=200)
    driver_name = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    station_assigned = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    vehicle_assigned = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True, related_name='+')
    details = models.TextField(blank = True, null=True)
    action_taken = models.TextField(blank = True, null=True)
    date_logged = models.DateTimeField(default=timezone.now, null=True)
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'incident_register', null=True)

    def __str__(self):
        return self.occurence_topic

    def get_absolute_url(self):
        # returns  to the vehicle list 
        return reverse('driver-incidents-list')

#models to test multiplication of form fields

class Testfuelname (models.Model):
    fuel_name = models.CharField(max_length=200, null = True) 

    def __str__(self):
        return self.fuel_name

class Testfuelprice (models.Model):
    fuel_name = models.ForeignKey(Testfuelname, on_delete=models.CASCADE, null=True) 
    fuel_price = models.DecimalField(max_digits=8, decimal_places=2) 
    date_entered = models.DateTimeField(auto_now=True, null=True)

class TestM(models.Model):

    fuel_name = models.ForeignKey(Testfuelname, on_delete=models.CASCADE, null=True)
    fuel_price = models.ForeignKey(Testfuelprice, on_delete=models.CASCADE, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    
    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        #  
        return reverse('test-list') 

class Fuel_mgt_update(models.Model):

    request_reference = models.UUIDField(default=uuid.uuid4)
    region = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    registration_no = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True, related_name='+')
    fuel_type_requested = models.ForeignKey(Fuel_name, on_delete=models.CASCADE, null = True)
    price_per_liter = models.ForeignKey(Fuel_price, on_delete=models.CASCADE, null = True)
    fuel_amount_requested = models.DecimalField(max_digits=8, decimal_places=2)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'requester2', null=True)
    date_requested = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'approver2', null=True)
    date_approved = models.DateTimeField(auto_now=True, null=True)
    closed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'fueler2',  null=True)
    fuel_issue_complete = models.BooleanField(default=False)
    date_closed = models.DateTimeField(default=timezone.now)
    declined = models.BooleanField(default=False)
    reason = models.TextField(blank = True, null=True)
    barcode = models.ImageField(upload_to='images/', null=True, blank=True)
    station_name = models.ForeignKey(Fuel_station, on_delete=models.CASCADE, null = True)
    driver_name = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    liters_served = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)    
    current_mileage = models.CharField(max_length=100, null=True, blank=True)
    attended_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'attendant2', null=True)
    date_fueled = models.DateTimeField(default=timezone.now)
    region_code = models.ForeignKey(UserUnit, on_delete=models.CASCADE, related_name = 'rcode2', null=True)
    station_mileage = models.CharField(max_length=100, null=True)
    fprice =  models.CharField(max_length=100, null=True)
  


    def __str__(self):
        return self.registration_no.registration_no

    def get_absolute_url(self):
        # returns us to the list view. can also set this to app-home
        return reverse('fuel-mgt-list')

class Motor_Cycle_Make (models.Model):
    SUZUKI = 'Suzuki'
    YAMAHA = 'Yamaha'

    MOTOR_CYCLE_MAKE = [
        (SUZUKI, ('Suzuki')),
        (YAMAHA, ('Yamaha')),

    ]

    motor_cycle_make = models.CharField(
        max_length=200,
        choices=MOTOR_CYCLE_MAKE,
        default=SUZUKI,
        unique=True
    )
    def __str__(self):
        return self.motor_cycle_make

class Motor_Cycle_Model (models.Model):
    DT125 = 'dt125'
    TF125 = 'tf125'
   

    MOTORCYCLE_MODEL = [
        (DT125, ('dt125')),
        (TF125, ('tf125')),

    ]    
    motor_cycle_make = models.ForeignKey(Motor_Cycle_Make, on_delete=models.CASCADE, null=True) 
    Motor_cycle_model = models.CharField(
        max_length=200,
        choices=MOTORCYCLE_MODEL,
        default=DT125,
        
    )
    motor_cycle_reg_no = models.CharField(max_length=100, unique=True, null=True)
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_registered = models.DateTimeField(auto_now=True, null=True)
    region = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    fuel_type = models.ForeignKey(Fuel_name, on_delete=models.CASCADE, null = True)
    fuel_capacity = models.CharField(max_length=100, null=True)
    engine_no = models.CharField(max_length=100, null=True)
    tank_capacity = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.motor_cycle_reg_no

    def get_absolute_url(self):
        # returns us to the list view. can also set this to app-home
        return reverse('list-riders')

class Rider (models.Model):

    HEADQUARTERS = 'Headquarters'
    EASTERN_REGION = 'Eastern Region'
    CENTRAL_REGION = 'Central Region'    
    NORTHERN_REGION = 'Northern Region'
    NORTH_EASTERN = 'North Eastern'
    SOUTHERN_REGION = 'Southern Region'
    WESTERN_REGION = 'Western Region'
    INFORMAL_SETTLEMENT_REGION = 'Informal Settlements Region'
    RUAI = 'Ruai'
    GIGIRI = 'Gigiri'
    KABETE_LABORATORY = 'Kabete Laboratory'
    KABETE_TREATMENT_WORKS = 'Kabete Treatment Works'
    RUIRU_DAM = 'Ruiru Dam'
    NGETHU_TREATMENT_WORKS = 'Ngethu Treatment Works'
    THIKA_DAM = 'Thika Dam'
    SASUMUA_TREATMENT_WORKS = 'Sasumua Treatment Works'
    KARIOBANGI_TREATMENT_WORKS = 'Kariobangi Treatment Works'
    NRW = 'Non Revenue Water'
    MALE = 'Male'
    FEMALE = 'Female'
    DRIVER = 'Driver'
    PLANT_OPERATOR = 'Plant operator'

    REGIONS = [
        (HEADQUARTERS, ('Headquarters')),
        (EASTERN_REGION, ('Eastern Region')),
        (CENTRAL_REGION, ('Central Region')),
        (NORTHERN_REGION, ('Northern Region')),
        (NORTH_EASTERN, ('North Eastern')),
        (SOUTHERN_REGION, ('Southern Region')),
        (WESTERN_REGION, ('Western Region')),
        (INFORMAL_SETTLEMENT_REGION, ('Informal Settlements Region')),
        (RUAI, ('Ruiru Dam')),
        (GIGIRI, ('Gigiri')),
        (KABETE_LABORATORY, ('Kabete Laboratory')),
        (RUIRU_DAM, ('Ruiru Dam')),
        (NGETHU_TREATMENT_WORKS, ('Ngethu Treatment Works')),
        (THIKA_DAM, ('Thika Dam')),
        (SASUMUA_TREATMENT_WORKS, ('Sasumua Treatment Works')),
        (KARIOBANGI_TREATMENT_WORKS, ('Kariobangi Treatment Works')),
        (NRW, ('Non Revenue Water')),
    ]

    GENDER = [
        (MALE, ('Male')),
        (FEMALE, ('Female')),
    ]


    full_name = models.CharField(max_length=100, unique=True)
    pf_no = models.CharField(max_length=100, unique=True )
    region_assigned = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    license_number = models.CharField(max_length=100, unique=True)
    expiry_date = models.DateField()
    assigned_motorcycle = models.ForeignKey(Motor_Cycle_Model, on_delete=models.CASCADE, null = True)
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.full_name

class Generator (models.Model):

    HEADQUARTERS = 'Headquarters'
    EASTERN_REGION = 'Eastern Region'
    CENTRAL_REGION = 'Central Region'    
    NORTHERN_REGION = 'Northern Region'
    NORTH_EASTERN = 'North Eastern'
    SOUTHERN_REGION = 'Southern Region'
    WESTERN_REGION = 'Western Region'
    INFORMAL_SETTLEMENT_REGION = 'Informal Settlements Region'
    RUAI = 'Ruai'
    GIGIRI = 'Gigiri'
    KABETE_LABORATORY = 'Kabete Laboratory'
    KABETE_TREATMENT_WORKS = 'Kabete Treatment Works'
    RUIRU_DAM = 'Ruiru Dam'
    NGETHU_TREATMENT_WORKS = 'Ngethu Treatment Works'
    THIKA_DAM = 'Thika Dam'
    SASUMUA_TREATMENT_WORKS = 'Sasumua Treatment Works'
    KARIOBANGI_TREATMENT_WORKS = 'Kariobangi Treatment Works'


    REGIONS = [
        (HEADQUARTERS, ('Headquarters')),
        (EASTERN_REGION, ('Eastern Region')),
        (CENTRAL_REGION, ('Central Region')),
        (NORTHERN_REGION, ('Northern Region')),
        (NORTH_EASTERN, ('North Eastern')),
        (SOUTHERN_REGION, ('Southern Region')),
        (WESTERN_REGION, ('Western Region')),
        (INFORMAL_SETTLEMENT_REGION, ('Informal Settlements Region')),
        (RUAI, ('Ruiru Dam')),
        (GIGIRI, ('Gigiri')),
        (KABETE_LABORATORY, ('Kabete Laboratory')),
        (RUIRU_DAM, ('Ruiru Dam')),
        (NGETHU_TREATMENT_WORKS, ('Ngethu Treatment Works')),
        (THIKA_DAM, ('Thika Dam')),
        (SASUMUA_TREATMENT_WORKS, ('Sasumua Treatment Works')),
        (KARIOBANGI_TREATMENT_WORKS, ('Kariobangi Treatment Works')),
    ]

    serial_number = models.CharField(max_length=200, unique=True)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    location = models.CharField(
        max_length=200,
        choices=REGIONS,
        default=HEADQUARTERS,
    )
    output = models.CharField(max_length=200)
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    fuel_capacity = models.CharField(max_length=200, null=True, blank=True)
     
    def __str__(self):
        return self.serial_number

    def get_absolute_url(self):
        # returns us to the list view. can also set this to app-home
        return reverse('list-generators')   

class Vendor (models.Model):

    vendor_name= models.CharField(max_length=200)

    def __str__(self):
        return self.vendor_name
        
class Vendor_station (models.Model):

    vendor_name = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    vendor_location = models.ForeignKey(Fuel_station, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.vendor_location.fuel_station_name

class Vendor_fuel_types (models.Model):

    vendor_name = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    fuel_type =  models.ForeignKey(Fuel_name, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.fuel_type.fuel_name

class Vendor_price (models.Model):

    vendor_name = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True) 
    fuel_name = models.ForeignKey(Vendor_fuel_types, on_delete=models.CASCADE, null=True) 
    fuel_price = models.FloatField(blank=True, null=True)
    discount_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.vendor_name.vendor_name 

class Fuel_mgt_m (models.Model):

    request_reference = models.UUIDField(default=uuid.uuid4)
    region = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    registration_no = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True, related_name='+')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null = True)
    vendor_location =  models.ForeignKey(Vendor_station, on_delete=models.CASCADE, null = True)
    fuel_type_requested = models.ForeignKey(Vendor_fuel_types, on_delete=models.CASCADE, related_name = 'fueltype', null = True)
    fuel_amount_requested = models.DecimalField(max_digits=8, decimal_places=2)
    price_per_liter = models.ForeignKey(Vendor_price, on_delete=models.CASCADE, related_name = 'fuelprice', null = True)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'frequester1', null=True)
    date_requested = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'fapprover1', null=True)
    date_approved = models.DateTimeField(auto_now=True, null=True)
    closed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'ffueler1',  null=True)
    fuel_issue_complete = models.BooleanField(default=False)
    date_closed = models.DateTimeField(default=timezone.now)
    declined = models.BooleanField(default=False)
    reason = models.TextField(blank = True, null=True)
    barcode = models.ImageField(upload_to='images/', null=True, blank=True)
    fuel_station_name = models.ForeignKey(Fuel_station, on_delete=models.CASCADE, null = True)
    driver_name = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    liters_served = models.IntegerField(null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)    
    attended_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'fattendant', null=True)
    date_fueled = models.DateTimeField(default=timezone.now)
    region_code = models.ForeignKey(UserUnit, on_delete=models.CASCADE, related_name = 'frcode', null=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    fprice =  models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.registration_no.registration_no

    def get_fuel_issued_price(self):
        return self.liters_served * self.price_per_liter.fuel_price

class Fuel_mgt_xn (models.Model):

    NEW="NEW" #new
    HR_APPROVED='HR-APPROVED' #HR-approved
    BPO_APPROVED='BPO-APPROVED' #BPo-approved
    FUELED='FUELED'#fueled
    BULK_FUEL = 'Bulk fuel'
    MOTOR_VEHICLE = 'Motor vehicle'
    
    STATUS_CHOICES = [
        (NEW, 'NEW'),
        (HR_APPROVED, 'HR-APPROVED'),
        (BPO_APPROVED, 'BPO-APPROVED'),
        (FUELED, 'FUELED'),    
    ]

    CATEGORY_CHOICES = [
        ('BULK_FUEL', 'Bulk Fuel'),
        ('MOTOR_VEHICLE', 'Motor Vehicle'),
    ]
    request_reference = models.UUIDField(default=uuid.uuid4)
    region = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    registration_no = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True, related_name='+')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null = True)
    vendor_location =  models.ForeignKey(Vendor_station, on_delete=models.CASCADE, null = True, related_name='+')
    fuel_type_requested = models.ForeignKey(Vendor_fuel_types, on_delete=models.CASCADE, related_name = 'xnfueltype', null = True)
    fuel_amount_requested = models.DecimalField(max_digits=8, decimal_places=2)
    price_per_liter = models.ForeignKey(Vendor_price, on_delete=models.CASCADE, related_name = 'xnfuelprice', null = True, blank=True)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    date_requested = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    date_approved = models.DateTimeField(auto_now=True, null=True)
    closed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+',  null=True)
    fuel_issue_complete = models.BooleanField(default=False)
    date_closed = models.DateTimeField(default=timezone.now)
    declined = models.BooleanField(default=False)
    reason = models.TextField(blank = True, null=True)
    barcode = models.ImageField(upload_to='images/', null=True, blank=True)
    fuel_station_name = models.ForeignKey(Fuel_station, on_delete=models.CASCADE, related_name='+', null = True)
    driver_name = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, related_name='+')
    previous_liters_served = models.CharField(max_length=100, null=True) 
    liters_served = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)    
    previous_mileage = models.CharField(max_length=100, null=True, blank=True)
    current_mileage = models.CharField(max_length=100, null=True, blank=True)
    distance_covered = models.IntegerField(null=True, blank=True)
    attended_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    date_fueled = models.DateTimeField(default=timezone.now)
    region_code = models.ForeignKey(UserUnit, on_delete=models.CASCADE, related_name='+', null=True)
    station_mileage = models.CharField(max_length=100, null=True, blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    fprice =  models.CharField(max_length=100, null=True)
    discount = models.ForeignKey(Vendor_price, on_delete=models.CASCADE, related_name = 'discountprice', null = True) 
    assign_request =  models.ForeignKey(User, null=True,blank=True, on_delete=models.SET_NULL)
    work_ticket_number = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    BPO_approval= models.BooleanField(default=False)
    approved_by_BPO = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    date_BPO_approved = models.DateTimeField(auto_now=True, null=True)
    fuel_Img = models.ImageField(upload_to='images/', null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,null=True,blank=True,default= NEW)
    fuel_consumed = models.IntegerField(null=True, blank=True)
    average_consumption = models.FloatField(null=True, blank=True)
    site_image = models.ImageField(upload_to='images/', null=True, blank=True)  # renamed field
    previous_worksheet = models.FileField(upload_to='documents/', null=True, blank=True)
    engine_hours = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True)###remove this field in prod
    bulk_fuel_quantity = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True) ###remove this filed in prod
    previous_bulk_fuel_quantity = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)####remove this field in prod


    def get_fuel_issued_price(self):

        if self.liters_served is not None:    
        
            #create variable tprice to store value and return true if condition is met
            #return 0 as a safe fall back if false
            tprice = self.liters_served * self.price_per_liter.fuel_price

            return tprice
        return 0

    def get_discount_total(self):
        
        #run the equation in a try block to make sure you do not return nonetype error
        try:
           d_price = (self.price_per_liter.fuel_price - self.discount.discount_price) * self.liters_served
        except:
            d_price = '0'

        return d_price
    
    def calculate_average_consumption(self):
        if self.distance_covered and self.previous_liters_served:
            self.average_consumption = self.distance_covered / float(self.previous_liters_served)
        else:
            self.average_consumption = None
            
    def get_absolute_url(self):
        # returns us to the list view. can also set this to app-home
        return reverse('fuel-mgtm-list')
    
    def save(self, *args, **kwargs):
        self.calculate_average_consumption()
        if self.previous_mileage and self.current_mileage:
            self.distance_covered = int(self.current_mileage) - int(self.previous_mileage)

        if self.previous_liters_served and self.liters_served:
            self.fuel_consumed = int(self.liters_served) - int(self.previous_liters_served)

        # if self.distance_covered and self.fuel_consumed:
        #     self.average_consumption = self.distance_covered / self.fuel_consumed

        super().save(*args, **kwargs)

    def __str__(self):
        return self.registration_no.registration_no

class Parts_stock (models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Parts_category (models.Model):
    ENGINE = 'engine'
    SUSPENSION = 'suspension'
    BODY = 'body'
    HLIGHTS = 'head_lights'
    SLIGHTS = 'side_lights'
    RLIGHTS = 'rear_lights'
    ELECTRICAL = 'electrical'
    BUSHES = 'bushing'
    EMIRRORS = 'mirrors_external'
    IMIRRORS = 'mirrors_internal'
    SCREEN = 'screen'
    BRAKES = 'brakes'
    TYRES = 'Tyres'
    TUBING = 'Tubing'
    SEAT = 'seat'
    WIPERARMS = 'wiper_arms'
    WIPERBLADES = 'wiper_blades'


    CATEGORY = [
        (ENGINE, ('engine')),
        (SUSPENSION, ('suspension')),
        (BODY, ('body')),
        (HLIGHTS, ('head_lights')),
        (SLIGHTS, ('side_lights')),
        (ELECTRICAL, ('electrical')),
        (BUSHES, ('bushing')),
        (EMIRRORS, ('mirrors_external')),
        (IMIRRORS, ('mirrors_internal')),
        (SCREEN, ('screen')),
        (BRAKES, ('brakes')),
        (TYRES, ('Tyres')),
        (TUBING, ('Tubing')),
        (SEAT, ('seat')),
        (WIPERARMS, ('wiper_arms')),
        (WIPERBLADES, ('wiper_blades')),

    ]


    name = models.ForeignKey(Parts_stock, on_delete=models.CASCADE, null = True)
    category = models.CharField(
        max_length=200,
        choices=CATEGORY,
        default=None,
    )
    serial_number = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name.name

class Garage (models.Model):

    issue_reference = models.UUIDField(default=uuid.uuid4)
    Vehicle_issue_topic = models.CharField(max_length=100, null=True)
    vehicle_registration_number = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True)
    make = models.ForeignKey(Make, on_delete=models.CASCADE, null = True)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null = True)
    vehicle_issue =  models.TextField(blank = True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = '+', null=True)
    date_created = models.DateTimeField(default=timezone.now)
    driver_assigned = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name = '+', null = True)
    region = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    mechanic = models.ForeignKey(User, on_delete=models.CASCADE, related_name = '+', null=True)
    vehicle_in = models.BooleanField(default=False)
    declined = models.BooleanField(default=False)
    reason_for_decline = models.TextField(blank = True, null=True)
    current_mileage = models.CharField(max_length=100, null=True)
    next_service = models.CharField(max_length=100, null=True)
    date_received = models.DateTimeField(default=timezone.now)
    service = models.BooleanField(default=False)
    works_description = models.TextField(blank = True, null=True)
    service_total = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    repair = models.BooleanField(default=False)
    parts = models.ForeignKey(Parts_stock, on_delete=models.CASCADE, null = True)
    quantity = models.IntegerField(default = 0)
    parts_requisition_date = models.DateTimeField(default=timezone.now)
    parts_received_date = models.DateTimeField(default=timezone.now)
    further_works_required_remarks = models.TextField(blank = True, null=True)
    vehicle_out = models.BooleanField(default=False)
    date_released = models.DateTimeField(default=timezone.now)
    down_time = models.CharField(max_length=100, null=True)
    transport_assistant = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'tra', null=True)
    transport_supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'trs', null=True)
    transport_officer = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'tro', null=True)
    mechanic_assesment = models.TextField(blank = True, null=True)
    approve_works = models.BooleanField(default=False)
    check_report = models.BooleanField(default=False)
    parts_required = models.TextField(blank = True, null=True)
    parts_installed = models.BooleanField(default=False)
    vehicle_released = models.BooleanField(default=False)
    def __str__(self):
        return self.Vehicle_issue_topic

    #def get_absolute_url(self):
        # returns  to the vehicle list 
        #return reverse('v-issue-list')

#messaging functionality        
class ThreadModel(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
  receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
  has_unread = models.BooleanField(default=False)

class MessageModel(models.Model):
  thread = models.ForeignKey('ThreadModel', related_name='+', on_delete=models.CASCADE, blank=True, null=True)
  sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
  receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
  body = models.CharField(max_length=1000)
  image = models.ImageField(upload_to='', blank=True, null=True)
  date = models.DateTimeField(default=timezone.now)
  is_read = models.BooleanField(default=False)

class Notification(models.Model):
    message = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey('Fuel_mgt_xn', on_delete=models.CASCADE)

    def __str__(self):
        return self.message
    
class Motor_bike_make(models.Model):
    SUZUKI = 'Suzuki'
    YAMAHA = 'Yamaha'

    MOTOR_CYCLE_MAKE = [
        (SUZUKI, ('Suzuki')),
        (YAMAHA, ('Yamaha')),

    ]

    motor_bike_make = models.CharField(
        max_length=200,
        choices=MOTOR_CYCLE_MAKE,
        default=SUZUKI,
        unique=True
    )
    def __str__(self):
        return self.motor_bike_make
    
class Motor_bike_model(models.Model):
    DT125 = 'dt125'
    TF125 = 'tf125'
   

    MOTORCYCLE_MODEL = [
        (DT125, ('dt125')),
        (TF125, ('tf125')),

    ]    
    motor_cycle_make = models.ForeignKey(Motor_bike_make, on_delete=models.CASCADE, null=True) 
    motor_cycle_model = models.CharField(
        max_length=200,
        choices=MOTORCYCLE_MODEL,
        default=DT125,
        
    )
    def __str__(self):
        return self.motor_cycle_model

class Motor_bike_register(models.Model):
    motor_cycle_reg_no = models.CharField(max_length=100, unique=True, null=True)
    date_registered = models.DateTimeField(auto_now=True, null=True)
    region = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    fuel_type = models.ForeignKey(Fuel_name, on_delete=models.CASCADE, null = True)
    engine_no = models.CharField(max_length=100, null=True, blank=True)
    tank_capacity = models.CharField(max_length=100, null=True)
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    make = models.ForeignKey(Motor_bike_make, on_delete=models.CASCADE, null = True)
    model = models.ForeignKey(Motor_bike_model, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.motor_cycle_reg_no
    
    def get_absolute_url(self):
        # returns us to the list view. can also set this to app-home
        return reverse('bikes-list')

class Motor_bike_riders(models.Model):
    rider_name = models.CharField(max_length=100, null=True)
    pf_no = models.CharField(max_length=100, null=True, unique=True)
    region = models.ForeignKey(station, on_delete=models.CASCADE, null = True) 


    def __str__(self):
        return self.rider_name

class Motor_bike_assignment_register(models.Model):
    rider_name = models.ForeignKey(Motor_bike_riders, on_delete=models.CASCADE, null = True)
    motor_cycle_reg_no = models.OneToOneField(Motor_bike_register, on_delete=models.CASCADE, null = True, unique=True)

    def __str__(self):
        return self.rider_name.rider_name

class Fuel_mgt_mb (models.Model):

    request_reference = models.UUIDField(default=uuid.uuid4)
    region = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    motor_cycle_reg_no = models.ForeignKey(Motor_bike_register, on_delete=models.CASCADE, null = True, related_name='+')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null = True)
    vendor_location =  models.ForeignKey(Vendor_station, on_delete=models.CASCADE, null = True, related_name='+')
    fuel_type_requested = models.ForeignKey(Vendor_fuel_types, on_delete=models.CASCADE, related_name = 'mbfueltype', null = True)
    fuel_amount_requested = models.DecimalField(max_digits=8, decimal_places=2)
    price_per_liter = models.ForeignKey(Vendor_price, on_delete=models.CASCADE, related_name = 'mbfuelprice', null = True, blank=True)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    date_requested = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    date_approved = models.DateTimeField(auto_now=True, null=True)
    closed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+',  null=True)
    fuel_issue_complete = models.BooleanField(default=False)
    date_closed = models.DateTimeField(default=timezone.now)
    declined = models.BooleanField(default=False)
    reason = models.TextField(blank = True, null=True)
    barcode = models.ImageField(upload_to='images/', null=True, blank=True)
    fuel_station_name = models.ForeignKey(Fuel_station, on_delete=models.CASCADE, related_name='+', null = True)
    rider_name = models.ForeignKey(Motor_bike_riders, on_delete=models.CASCADE, null=True, related_name='+')
    previous_liters_served = models.CharField(max_length=100, null=True) 
    liters_served = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)    
    previous_mileage = models.CharField(max_length=100, null=True, blank=True)
    current_mileage = models.CharField(max_length=100, null=True, blank=True)
    distance_covered = models.CharField(max_length=100, null=True)
    attended_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    date_fueled = models.DateTimeField(default=timezone.now)
    region_code = models.ForeignKey(UserUnit, on_delete=models.CASCADE, related_name='+', null=True)
    station_mileage = models.CharField(max_length=100, null=True, blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    fprice =  models.CharField(max_length=100, null=True)
    discount = models.ForeignKey(Vendor_price, on_delete=models.CASCADE, related_name = 'mbdiscountprice', null = True) 
    assign_request = models.ManyToManyField(User)
    work_ticket_number = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    BPO_approval= models.BooleanField(default=False)
    approved_by_BPO = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    date_BPO_approved = models.DateTimeField(auto_now=True, null=True)
    fuel_Img = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.motor_cycle_reg_no.motor_cycle_reg_no

    def get_fuel_issued_price(self):

        if self.liters_served is not None:    
        
            #create variable tprice to store value and return true if condition is met
            #return 0 as a safe fall back if false
            tprice = self.liters_served * self.price_per_liter.fuel_price

            return tprice
        return 0

    def get_discount_total(self):
        
        #run the equation in a try block to make sure you do not return nonetype error
        try:
           d_price = (self.price_per_liter.fuel_price - self.discount.discount_price) * self.liters_served
        except:
            d_price = '0'

        return d_price


    # def get_absolute_url(self):
    #     # returns us to the list view. can also set this to app-home
    #     return reverse('fuel-mgtm-list')
    
class Motor_cycle_issues (models.Model):

    issue_reference = models.UUIDField(default=uuid.uuid4)
    motor_cycle_topic = models.CharField(max_length=100, null=True)
    motor_cycle_registration_number = models.ForeignKey(Motor_bike_register, on_delete=models.CASCADE, null = True)
    motor_cycle_issue =  models.TextField(blank = True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = '+', null=True)
    date_created = models.DateTimeField(default=timezone.now)
    rider_assigned = models.ForeignKey(Motor_bike_riders, on_delete=models.CASCADE, related_name = '+', null = True)
    region = models.ForeignKey(station, on_delete=models.CASCADE, null = True)
    mechanic = models.ForeignKey(User, on_delete=models.CASCADE, related_name = '+', null=True)
    motor_cycle_in = models.BooleanField(default=False)
    declined = models.BooleanField(default=False)
    reason_for_decline = models.TextField(blank = True, null=True)
    current_mileage = models.CharField(max_length=100, null=True)
    next_service = models.CharField(max_length=100, null=True)
    date_received = models.DateTimeField(default=timezone.now)
    service = models.BooleanField(default=False)
    works_description = models.TextField(blank = True, null=True)
    service_total = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    repair = models.BooleanField(default=False)
    repair_description = models.TextField(blank = True, null=True)
    works_total = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    parts_requisition_date = models.DateTimeField(default=timezone.now)
    parts_received_date = models.DateTimeField(default=timezone.now)
    further_works_required_remarks = models.TextField(blank = True, null=True)
    vehicle_out = models.BooleanField(default=False)
    date_released = models.DateTimeField(default=timezone.now)
    down_time = models.CharField(max_length=100, null=True)
    transport_assistant = models.ForeignKey(User, on_delete=models.CASCADE, related_name = '+', null=True)
    transport_supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name = '+', null=True)
    transport_officer = models.ForeignKey(User, on_delete=models.CASCADE, related_name = '+', null=True)
    mechanic_assesment = models.TextField(blank = True, null=True)
    approve_works = models.BooleanField(default=False)
    check_report = models.BooleanField(default=False)
    parts_required = models.TextField(blank = True, null=True)

    def __str__(self):
        return self.motor_cycle_topic

    # def get_absolute_url(self):
    #     # returns  to the vehicle list 
    #     return reverse('mb-issue-list')

class Bulk_Fuel_Request(models.Model):
    request_reference = models.UUIDField(default=uuid.uuid4)
    region = models.ForeignKey(station, on_delete=models.CASCADE)
    registration_no = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, related_name='+')
    driver_name = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='+')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    vendor_location =  models.ForeignKey(Vendor_station, on_delete=models.CASCADE, related_name='+')
    fuel_type_requested = models.ForeignKey(Vendor_fuel_types, on_delete=models.CASCADE, related_name = 'bulkfueltype')
    fuel_amount_requested = models.DecimalField(max_digits=8, decimal_places=2)
    price_per_liter = models.ForeignKey(Vendor_price, on_delete=models.CASCADE, related_name = 'bulkfuelprice')
    current_plant_hours = models.CharField(max_length=100)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    date_requested = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    assign_request =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    BPO_approval= models.BooleanField(default=False)
    approved_by_BPO = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    date_BPO_approved = models.DateTimeField(auto_now=True, null=True)
    date_approved = models.DateTimeField(auto_now=True, null=True)
    closed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    fuel_issue_complete = models.BooleanField(default=False)
    date_closed = models.DateTimeField(default=timezone.now)
    declined = models.BooleanField(default=False)
    reason = models.TextField(blank = True, null=True)
    fuel_station_name = models.ForeignKey(Fuel_station, on_delete=models.CASCADE, related_name='+')
    previous_liters_served = models.CharField(max_length=100, null=True) 
    liters_served = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)    
    attended_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True)
    date_fueled = models.DateTimeField(default=timezone.now)
    region_code = models.ForeignKey(UserUnit, on_delete=models.CASCADE, related_name='+', null=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    fprice =  models.CharField(max_length=100, null=True)
    discount = models.ForeignKey(Vendor_price, on_delete=models.CASCADE, related_name = 'bulkdiscountprice', null = True) 


    def get_fuel_issued_price(self):

        if self.liters_served is not None:    
        
            #create variable tprice to store value and return true if condition is met
            #return 0 as a safe fall back if false
            tprice = self.liters_served * self.price_per_liter.fuel_price

            return tprice
        return 0

    def get_discount_total(self):
        
        #run the equation in a try block to make sure you do not return nonetype error
        try:
           d_price = (self.price_per_liter.fuel_price - self.discount.discount_price) * self.liters_served
        except:
            d_price = '0'

        return d_price
    
    def __str__(self):
        return self.region