from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin
from .models import (Vehicle_register, 
                    Driver, Assign_fuel, 
                    Request_fuel, 
                    station, 
                    Fuel_price, 
                    Fuel_name, 
                    Fuel_mgt,
                    Fuel_mgt_update, 
                    Fuel_station, 
                    Vehicle_issues, 
                    Vehicle_handover, 
                    UserUnit,
                    Driver_Incidents,
                    Mechanic_reg,
                    Country,
                    City, 
                    Person,
                    TestM,
                    Testfuelname,
                    Testfuelprice,
                    Model,
                    Make,
                    Motor_Cycle_Make,
                    Motor_Cycle_Model,
                    Generator,
                    Rider,
                    Vendor,
                    Vendor_station,
                    Vendor_price,
                    Fuel_mgt_m,
                    Fuel_mgt_xn,
                    Vendor_fuel_types,
                    Parts_stock,
                    Parts_category,
                    Garage,
                    Motor_bike_make,
                    Motor_bike_model,
                    Motor_bike_register,
                    Motor_bike_riders,
                    Motor_bike_assignment_register,
                    Fuel_mgt_mb,
                    Motor_cycle_issues, 
                    Bulk_Fuel_Request)

# Register your models here.
admin.site.site_header = 'NCWSC TRANSPORT SYSTEM'

class GeneratorAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['serial_number', 'make', 'model', 'location', 'output']

class RiderAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['full_name', 'pf_no', 'region_assigned', 'license_number', 'expiry_date', 'assigned_motorcycle', 'entered_by']

@admin.register(station)
class stationAdmin(admin.ModelAdmin):
    list_display = ['station']

@admin.register(Vehicle_register)
class Vehicle_RegisterAdmin(admin.ModelAdmin):
    search_fields = ['registration_no', 'chassis_number', 'region', 'make', 'model']
    list_display = ("registration_no", "chassis_number", "region", "make", "model", "type", "body_type", "fuel_type", "manufacture_year",
                         "engine_capacity", "engine_no", "color", "vehicle_registration_date", "gross_weight", "passengers",
                          "tare_weight", "tax_class", "axles", "load_capacity", "operational_status", "log_book_number", "registered_by", "date_registered")

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    search_fields = ['full_name']
    list_display = ("full_name", "pf_no", "gender", "region_assigned", "license_number",
                         "expiry_date", "job_title", "driver_history", "assigned_vehicle")

@admin.register(Assign_fuel)
class Assign_fuelAdmin(admin.ModelAdmin):
    list_display = ("station_name", "fuel_type", "price_per_liter", "liters_served", "previous_liters_served", 
                        "vehicle", "current_mileage", "amount", "entered_by", "date_posted", "station")

@admin.register(Request_fuel)
class Request_fuelAdmin(admin.ModelAdmin):
    list_display = ("fuel_request_reference", "vehicle_registration_number", "region", "fuel_type_requested", "fuel_amount_requested", "price_per_liter", 
                        "total", "requested_by", "date_requested", "approved", "approved_by", "date_approved", "closed_by", "fuel_issue_complete", "date_closed", "declined", "reason")
    
@admin.register(Fuel_price)
class Fuel_priceAdmin(admin.ModelAdmin):
    list_display = ("fuel_name", "fuel_price", "date_entered")

@admin.register(Vendor_price)
class Vendor_priceAdmin(admin.ModelAdmin):
    list_display = ("vendor_name", "fuel_name", "fuel_price", "discount_price")

@admin.register(Vendor_station)
class Vendor_stationAdmin(admin.ModelAdmin):
    list_display = ("vendor_name", "vendor_location")

@admin.register(Vendor_fuel_types)
class Vendor_fuel_typesAdmin(admin.ModelAdmin):
    list_display = ("vendor_name", "fuel_type")

@admin.register(Parts_stock)
class Parts_stockAdmin(admin.ModelAdmin):
    list_display = ("id","name")

@admin.register(Parts_category)
class Parts_categoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "serial_number")



admin.site.register(Fuel_name)
admin.site.register(Fuel_mgt)
admin.site.register(Fuel_mgt_update)
admin.site.register(Fuel_station)
admin.site.register(Vehicle_handover)
admin.site.register(UserUnit)
admin.site.register(Mechanic_reg)
admin.site.register(Person)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(TestM)
admin.site.register(Testfuelname)
admin.site.register(Testfuelprice)
admin.site.register(Model)
admin.site.register(Make)
admin.site.register(Rider, RiderAdmin)
admin.site.register(Generator, GeneratorAdmin)
admin.site.register(Vendor)
admin.site.register(Fuel_mgt_m)
admin.site.register(Fuel_mgt_xn)
admin.site.register(Garage)
admin.site.register(Motor_bike_make)
admin.site.register(Motor_bike_model)
admin.site.register(Motor_bike_register)
admin.site.register(Fuel_mgt_mb)
admin.site.register(Motor_cycle_issues)
admin.site.register(Bulk_Fuel_Request)



@admin.register(Vehicle_issues)
class Vehicle_issuesAdmin(admin.ModelAdmin):
    search_fields = ['issue_reference']
    list_display = ["issue_reference", "Vehicle_issue_topic", "vehicle_registration_number", "vehicle_issue", "mechanic_assesment"]
@admin.register(Driver_Incidents)
class Driver_IncidentsAdmin(admin.ModelAdmin):
    search_fields = ['driver_name']
    list_display = ["occurence_topic", "driver_name", "station_assigned", "details", "action_taken", "registered_by"]

#manage riders and motorbile assignements
@admin.register(Motor_bike_riders)
class Motor_bike_ridersAdmin(admin.ModelAdmin):
    search_fields = ['rider_name', 'pf_no']
    list_display = ["rider_name", "pf_no"]

@admin.register(Motor_bike_assignment_register)
class Motor_bike_assignment_registerAdmin(admin.ModelAdmin):
    search_fields = ['rider_name', 'motor_cycle_reg_no']
    list_display = ["rider_name", "motor_cycle_reg_no"]
