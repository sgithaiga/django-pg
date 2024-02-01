from django.urls import path
from . import views
from .views import ChartView

urlpatterns = [
    path('', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data', views.pivot_data, name='pivot_data'),
    path('chart-data/', ChartView.as_view(), name='chart_data'),
]