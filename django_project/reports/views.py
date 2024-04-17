from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Sum, F
from django.db.models import Count
from django.core import serializers
from django.db.models.functions import ExtractMonth, ExtractYear
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
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  TemplateView,
                                  View)

from rest_framework.views import APIView 
from rest_framework.response import Response 

from django.db.models.functions import TruncMonth

from transport.models import Vehicle_register, Driver, Request_fuel, Assign_fuel, Fuel_mgt, Fuel_mgt_xn, Vendor_fuel_types, Fuel_name
from .models import Historic_Consumption

from transport.forms import Assign_fuelForm, Request_fuelForm, Vehicle_registerForm

# Create your views here.


class chartView(View): 
    def get(self, request, *args, **kwargs): 
        return render(request, 'reports/chart-home.html')
    
class RegionChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'reports/region-chart-home.html')
    
class RegionFuelCostChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'reports/region-fuel-cost-chart.html')
# dont use
class ChartData(APIView): 
    authentication_classes = [] 
    permission_classes = [] 
   
    def get(self, request, format = None): 
        labels = [ 
            'January', 
            'February',  
            'March',  
            'April',  
            'May',  
            'June',  
            'July'
            ] 
        chartLabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45] 
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata, 
             } 
        return Response(data) 

class Fuel_mgt_issued_ListView(LoginRequiredMixin, ListView):
    model = Fuel_mgt_xn
    template_name = 'reports/vehicle_consumption.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_fueled']
    paginate_by = 10


def showresults(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        todate=request.POST.get('todate')
        searchresult=Fuel_mgt_xn.objects.raw("select id, registration_no_id,region_id,vendor_id,date_fueled,liters_served,fuel_type_requested_id,attended_by_id,vendor_location_id from transport_fuel_mgt_xn where date_fueled between '"+fromdate+"' and '"+todate+"'")
        return render(request, 'reports/vehicle_consumption_search.html',{"data":searchresult} )
    else:
        displaydata = Fuel_mgt_xn.objects.all()
        return render(request, 'reports/vehicle_consumption_search.html', {"data":displaydata} )

class FuelDataView(View):
    def get(self, request, *args, **kwargs):
        fuel_data = Fuel_mgt_xn.objects.only('previous_mileage', 'current_mileage', 'previous_liters_served', 'liters_served')

        for data in fuel_data:
            if data.previous_mileage and data.current_mileage:
                data.distance_covered = int(data.current_mileage) - int(data.previous_mileage)
            if data.previous_liters_served and data.liters_served:
                data.fuel_consumed = int(data.liters_served) - int(data.previous_liters_served)
            if data.distance_covered and data.previous_liters_served:
                data.average_consumption = data.distance_covered / float(data.previous_liters_served)

        return render(request, 'reports/fuel_data.html', {'fuel_data': fuel_data})



class RegistrationNumbersView(View):
    def get(self, request, *args, **kwargs):
        try:
            # Fetch the related Vehicle_register objects
            vehicles = Fuel_mgt_xn.objects.select_related('registration_no').distinct()

            # Extract the distinct registration numbers
            registration_numbers = list(set(vehicle.registration_no.registration_no for vehicle in vehicles))

            return JsonResponse(registration_numbers, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class ChartDataView(View):
    def get(self, request, *args, **kwargs):
        registration_no = request.GET.get('registration_no')
        if not registration_no:
            return JsonResponse({'error': 'Missing registration_no parameter'}, status=400)
        try:
            # Filter Fuel_mgt_xn objects based on the registration_no field of the related Vehicle_register model
            fuel_data = Fuel_mgt_xn.objects.filter(registration_no__registration_no=registration_no)
            chart_data = []
            for data in fuel_data:
                if data.previous_mileage and data.current_mileage:
                    data.distance_covered = int(data.current_mileage) - int(data.previous_mileage)
                if data.previous_liters_served and data.liters_served:
                    data.fuel_consumed = int(data.liters_served) - int(data.previous_liters_served)
                if data.distance_covered and data.previous_liters_served:
                    data.average_consumption = data.distance_covered / float(data.previous_liters_served)
                chart_data.append({
                    'date': data.date_requested.strftime('%Y-%m-%d'),  # Replace with the appropriate date field
                    'average_consumption': data.average_consumption,
                    'distance_covered': data.distance_covered,  # Add distance_covered to the response
                    'fuel_issued': data.liters_served,  # Add liters_served to the response
                })
            return JsonResponse(chart_data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class FuelIssuedPerRegionView(View):
    def get(self, request, *args, **kwargs):
        try:
            # Get the IDs for 'Diesel' and 'Petrol' from the Fuel_name model
            diesel_id = Fuel_name.objects.get(fuel_name='Diesel').id
            petrol_id = Fuel_name.objects.get(fuel_name='Petrol').id

            # Aggregate the total fuel issued per region for diesel
            diesel_data = Fuel_mgt_xn.objects.filter(fuel_type_requested__fuel_type_id=diesel_id).values('region__station').annotate(total_fuel_issued=Sum('liters_served'))

            # Aggregate the total fuel issued per region for petrol
            petrol_data = Fuel_mgt_xn.objects.filter(fuel_type_requested__fuel_type_id=petrol_id).values('region__station').annotate(total_fuel_issued=Sum('liters_served'))

            return JsonResponse({
                'diesel_data': list(diesel_data),
                'petrol_data': list(petrol_data),
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        



class MonthlyFuelIssuedPerRegionView(View):
    def get(self, request, *args, **kwargs):
        month = request.GET.get('month')
        year = request.GET.get('year')
        if not month or not year:
            return JsonResponse({'error': 'Missing month or year parameter'}, status=400)
        try:
            # Get the IDs for 'Diesel' and 'Petrol' from the Fuel_name model
            diesel_id = Fuel_name.objects.get(fuel_name='Diesel').id
            petrol_id = Fuel_name.objects.get(fuel_name='Petrol').id

            # Filter by month and year, and aggregate the total fuel issued per region for diesel
            diesel_data = Fuel_mgt_xn.objects.filter(
                fuel_type_requested__fuel_type_id=diesel_id,
                date_requested__month=month,
                date_requested__year=year
            ).values('region__station').annotate(total_fuel_issued=Sum('liters_served'))

            # Filter by month and year, and aggregate the total fuel issued per region for petrol
            petrol_data = Fuel_mgt_xn.objects.filter(
                fuel_type_requested__fuel_type_id=petrol_id,
                date_requested__month=month,
                date_requested__year=year
            ).values('region__station').annotate(total_fuel_issued=Sum('liters_served'))

            return JsonResponse({
                'diesel_data': list(diesel_data),
                'petrol_data': list(petrol_data),
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)




class FuelCostPerRegionView(View):
    def get(self, request, *args, **kwargs):
        # Query the database for fuel costs per region
        diesel_costs = Fuel_mgt_xn.objects.filter(fuel_type_requested__fuel_type__fuel_name='Diesel').values('region__rname').annotate(total_cost=Sum('total_price'))
        petrol_costs = Fuel_mgt_xn.objects.filter(fuel_type_requested__fuel_type__fuel_name='Petrol').values('region__rname').annotate(total_cost=Sum('total_price'))

        # Convert the querysets to dictionaries
        diesel_data = list(diesel_costs.values('region__station', 'total_cost'))
        petrol_data = list(petrol_costs.values('region__station', 'total_cost'))

        # Return the JSON response
        return JsonResponse({'diesel': diesel_data, 'petrol': petrol_data})
    
    
    
#view to handle historic consuption visualiation#
#return data in json

class ConsumptionAnalysisView(View):
    def get(self, request, *args, **kwargs):
        # Get consumption data grouped by month, region, fuel type, and calculate total quantity and cost
        consumption_data = Historic_Consumption.objects.annotate(
            month=TruncMonth('consumption_date')
        ).values('month', 'region', 'fuel_type').annotate(
            total_quantity=Sum('quantity'),
            total_cost=Sum(F('quantity') * F('cost_per_liter'))  # Calculate total cost
        )

        # Process the data to prepare for plotting
        data = {}
        for item in consumption_data:
            month = item['month'].strftime('%Y-%m')  # Convert date to string
            region = item['region']
            fuel_type = item['fuel_type']
            total_quantity = item['total_quantity']
            total_cost = item['total_cost']

            if month not in data:
                data[month] = {}

            if region not in data[month]:
                data[month][region] = {'Diesel': {'quantity': 0, 'cost': 0}, 'Petrol': {'quantity': 0, 'cost': 0}}

            data[month][region][fuel_type] = {'quantity': total_quantity, 'cost': total_cost}

        return JsonResponse(data)
    
#template for displaying regions analysis chart   
class ConsumptionAnalysisTemplateView(TemplateView):
    template_name = 'reports/consumption_analysis.html'
    

## grouping the data by month and registration_no, and calculating the total quantity. 
# The JSON data includes the total quantity for each registration_no for each month.
class RegistrationNoAnalysisView(View):
    def get(self, request, *args, **kwargs):
        # Get consumption data grouped by month, registration_no, and calculate total quantity and total amount
        consumption_data = Historic_Consumption.objects.annotate(
            month=TruncMonth('consumption_date')
        ).values('month', 'registration_no').annotate(
            total_quantity=Sum('quantity'),
            total_amount=Sum('total_amount')  # Calculate total amount
        )

        # Process the data to prepare for plotting
        data = {}
        for item in consumption_data:
            month = item['month'].strftime('%Y-%m')  # Convert date to string
            registration_no = item['registration_no']
            total_quantity = item['total_quantity']
            total_amount = item['total_amount']

            if month not in data:
                data[month] = {}

            data[month][registration_no] = {'quantity': total_quantity, 'amount': total_amount}

        return JsonResponse(data)
    
#template for displaying regions analysis chart   
class HistoricalRegistrationNoAnalysisView(TemplateView):
    template_name = 'reports/historic_vehicle_consumption_analysis.html'
    
class TotalRegistrationsView(TemplateView):
    template_name = 'reports/total_registrations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_registrations'] = Vehicle_register.objects.count()
        context['total_operational'] = Vehicle_register.objects.filter(operational_status='operational').count()
        context['total_grounded'] = Vehicle_register.objects.filter(operational_status='grounded').count()
        
        return context