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

from transport.models import station
from vehiclemgt.models import Vehicle_register
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
    expiry_date = models.DateField()
    driver_history = models.TextField()
    assigned_vehicle = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True)
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    job_title = models.CharField(max_length=100, choices=JOB_TITLE, null=True)

    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        # returns  to the vehicle list 
        return reverse('driver-list')
