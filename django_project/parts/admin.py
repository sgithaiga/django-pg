from django.contrib import admin
from . models import (Vehicle, Parts, 
                      TyreIssuance, 
                      AutoGarage, 
                      VehicleDispatch, 
                      VehicleAssessment, 
                      ImprestPartsAquisition)
# Register your models here.

admin.site.register(Vehicle)
admin.site.register(Parts)
admin.site.register(TyreIssuance)
admin.site.register(AutoGarage)
admin.site.register(VehicleDispatch)
admin.site.register(VehicleAssessment)
admin.site.register(ImprestPartsAquisition)