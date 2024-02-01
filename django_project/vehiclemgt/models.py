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

from transport.models import station, Fuel_name

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


    registration_no = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(station, on_delete=models.CASCADE, related_name='+', null=True)
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
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+', null=True) 
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
    type =  models.CharField(max_length=100, null=True)
    fuel_type = models.ForeignKey(Fuel_name, on_delete=models.CASCADE, related_name='+', null=True )


    def __str__(self):
        return self.registration_no

    def get_absolute_url(self):
        # returns  to the vehicle list 
        return reverse('vehicle-list')


