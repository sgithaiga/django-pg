from django.urls import path
from .views import  chartView, ChartData, Fuel_mgt_issued_ListView
from . import views
from .views import (FuelDataView, 
                    RegistrationNumbersView, 
                    ChartDataView,RegionChartView, 
                    FuelIssuedPerRegionView, 
                    MonthlyFuelIssuedPerRegionView, 
                    FuelCostPerRegionView, 
                    RegionFuelCostChartView,
                    ConsumptionAnalysisView,
                    ConsumptionAnalysisTemplateView,
                    RegistrationNoAnalysisView,
                    HistoricalRegistrationNoAnalysisView,
                    TotalRegistrationsView)

urlpatterns = [
    path('report_cons/', Fuel_mgt_issued_ListView.as_view(), name='report-consumption-list'),
    path('charts/', chartView.as_view(), name='chart-home'),#view fuel data for individual vehicles
    path('api/chart/data/', ChartData.as_view()), #api data do not use
    path('report_search/', views.showresults, name='report-consumption-search'),
    path('fuel_data/', FuelDataView.as_view(), name='fuel-data'),
    path('registration_no/', RegistrationNumbersView.as_view(), name='registration-no'), #jsonregistration no data
    path('chart_data/', ChartDataView.as_view(), name='chart-data'),    
    path('region_data/', FuelIssuedPerRegionView.as_view(), name='fuel-issued-per-region'), #return region json data
    path('region_chart/', RegionChartView.as_view(), name='region-chart'),#display regional fuel usage
    path('region_fuel_cost_chart/', RegionFuelCostChartView.as_view(), name='region-fuel-cost-chart'),#region chart pie chart
    path('monthly-fuel-issued-per-region/', MonthlyFuelIssuedPerRegionView.as_view(), name='monthly-fuel-issued-per-region'), #json
    path('fuel-cost-per-region/', FuelCostPerRegionView.as_view(), name='fuel_cost_per_region'), # json fuel cost per region   
    path('historic-consumption/', ConsumptionAnalysisView.as_view(), name='historic-consumption'),#returns historic consuption and cost per region as a json payload
    path('consumption-analysis/', ConsumptionAnalysisTemplateView.as_view(), name='consumption_analysis'), #display historic data   
    path('vehicle-historic-consumption/', RegistrationNoAnalysisView.as_view(), name='vehicle-historic-consumption'), #return historic consumption and cost per vehicle as json payload
    path('regno-consumption-analysis/', HistoricalRegistrationNoAnalysisView.as_view(), name='regno-consumption_analysis'), #individual consumption data in line graph
    path('total-registrations/', TotalRegistrationsView.as_view(), name='total_registrations'),
]