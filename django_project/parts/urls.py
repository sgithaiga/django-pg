from django.urls import path

from . import views

app_name = 'parts'

urlpatterns = [    
    path('', views.HomeView.as_view(), name='home'),
    path('vehicle/', views.VehicleListView.as_view(), name='list_vehicles'),
    path('vehicle/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle_detail'),
    path('vehicle/add/', views.VehicleCreateView.as_view(), name='add_vehicle'),
    # use this views for managing parts
    path('vehicle/parts_list/', views.VehiclePartsListView.as_view(), name='list-parts'),
    path('vehicle/parts_request_create/', views.partsrequestView.as_view(), name='parts-request'),
    path('vehicle/parts_request_detail/<int:pk>/', views.partsrequestDetailView.as_view(), name='part-request-details'),
    path('vehicle/parts_request_update/<int:pk>/', views.partsrequestUpdateView.as_view(), name='part-request-update'),
    path('vehicle/tyre_issuance/', views.TyreIssuanceCreateView.as_view(), name='tyre-issuance'),
    path('vehicle/tyre_issuance_list/', views.TyreIssuanceListView.as_view(), name='list-tyre-issuance'),
    
    #imperest parts management
    path('vehicle/imperest_request/', views.ImprestPartsAquisitionCreateView.as_view(), name='imperest-request'),
    path('vehicle/imperest_request_list/', views.ImprestPartsAquisitionListView.as_view(), name='list-imperest-requests'),
    path('vehicle/imperest_request_update/<int:pk>/', views.ImprestPartsAquisitiontUpdateView.as_view(), name='imperest-request-update'),
    path('vehicle/imperest_request_detail/<int:pk>/', views.ImprestPartsAquisitionDetailView.as_view(), name='imperest-request-detail'),
    
    #vehicle garage dispatch Date 
    path('vehicle/garage_dispatch/', views.VehicleDispatchCreateView.as_view(), name='garage-dipatch-create'),
    path('vehicle/garage_dispatch_list/', views.VehicleDispatchListView.as_view(), name='garage-dipatch-list'),
    path('vehicle/garage_dispatch_update/<int:pk>/', views.VehicleDispatchUpdateView.as_view(), name='garage-dipatch-update'),
]