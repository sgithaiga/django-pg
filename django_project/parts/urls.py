from django.urls import path

from . import views

app_name = 'parts'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('vehicle/', views.VehicleListView.as_view(), name='list_vehicles'),
    path('vehicle/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle_detail'),
    path('vehicle/add/', views.VehicleCreateView.as_view(), name='add_vehicle'),
    path('vehicle/<int:pk>/parts/edit/', views.VehiclePartsEditView.as_view(), name='vehicle_parts_edit'),
    path('vehicle/parts_list/', views.VehiclePartsListView.as_view(), name='list_parts'),
]