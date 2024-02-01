from django.urls import path
from .views import  chartView, ChartData, Fuel_mgt_issued_ListView
from . import views


urlpatterns = [
    path('report_cons/', Fuel_mgt_issued_ListView.as_view(), name='report-consumption-list'),
    path('charts/', chartView.as_view(), name='chart-home'),
    path('api/chart/data/', ChartData.as_view()),
    path('report_search/', views.showresults, name='report-consumption-search')
    ]