from django.shortcuts import render
from django.http import HttpResponse
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

from transport.models import Vehicle_register, Driver, Request_fuel, Assign_fuel, Fuel_mgt, Fuel_mgt_xn
from transport.forms import Assign_fuelForm, Request_fuelForm, Vehicle_registerForm

# Create your views here.


class chartView(View): 
    def get(self, request, *args, **kwargs): 
        return render(request, 'reports/chart-home.html')

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
        searchresult=Fuel_mgt_xn.objects.raw('select id, registration_no_id,region_id,vendor_id,date_fueled,liters_served,fuel_type_requested_id,attended_by_id,vendor_location_id from transport_fuel_mgt_xn where date_fueled between "'+fromdate+'" and "'+todate+'"')
        return render(request, 'reports/vehicle_consumption_search.html',{"data":searchresult} )
    else:
        displaydata = Fuel_mgt_xn.objects.all()
        return render(request, 'reports/vehicle_consumption_search.html', {"data":displaydata} )
