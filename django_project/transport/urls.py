from django.urls import path
from . import views
from .views import (Assign_fuelCreateView, 
                    #Assign_fuelListView, 
                    #SAssign_fueltDetailView, 
                    DriverListView, 
                    DriverDetailView, 
                    Vehicle_registerListView, 
                    Vehicle_registerDetailView, 
                    Vehicle_registerUpdateView,
                    Request_fuelCreateView, 
                    Request_fueltDetailView, 
                    Request_fuelListView,
                    UserRequest_fuelListView, 
                    Request_fuelUpdate,
                    Request_fuel_completeUpdate,
                    PermissionsView,
                    fuelapproval_render_pdf_view,
                    Vehicle_registerCreateView,
                    DriverCreateView,
                    DriverUpdateView, 
                    Request_fuel_declineUpdate,
                    Request_fuel_UpdateView,
                    Request_fuelDeleteView,
                    Vehicle_issuesCreateView,
                    Vehicle_issuesListView,
                    Fuel_mgtDeleteView,
                    Fuel_mgtListView,
                    UserFuel_mgtListView,
                    Fuel_mgtUpdateView,
                    Fuel_mgt_UpdateView,
                    Fuel_mgt_declineUpdate,
                    Fuel_mgt_completeUpdate,
                    Fuel_mgt_f_issue_UpdateView,
                    Fuel_mgtDetailView,
                    Fuel_mgt_updateCreateView,
                    Driver_IncidentsCreateView,
                    Driver_IncidentsListView,
                    Vehicle_issuesDetailView,
                    mechanic_assesmentUpdate,
                    work_assessmentUpdateView,
                    work_assessment_approvalUpdateView,
                    work_assessmentDetailView,
                    Motorcycle_CreateView,
                    Motorcycle_ListView,
                    Rider_CreateView,
                    Rider_ListView,
                    Generator_CreateView,
                    Reqfilter,
                    FormWizardView,
                    Fuel_mgtCreateView,
                    PersonCreateView,
                    TestMCreateView,
                    total,
                    TestMListView,
                    Fuel_mgt_mCreateView,
                    Fuel_mgt_mListView,
                    Fuel_mgt_mDetailView,
                    Fuel_mgt_mUpdateView,
                    Fuel_mgt_mcompleteUpdate,
                    Fuel_mgtmDeleteView,
                    Fuel_mgtm_declineUpdate,
                    Fuel_mgtm_f_issue_UpdateView,
                    Fuel_mgtmDetailView,
                    UserFuel_mgmtListView,
                    ListThreads,
                    CreateThread,
                    ThreadView,
                    CreateMessage,
                    Fuel_mgt_mBPOUpdateView,
                    Motorbike_registerCreateView,
                    Fuel_mgt_mbikeCreateView
                    )


urlpatterns = [
    path('', views.home_view, name='transport-home'),
    path('transport/drivers/', DriverListView.as_view(), name='driver-list'),
    path('transport/drivers_details/<int:pk>/', DriverDetailView.as_view(), name='driver-details'),
    path('transport/vehicles/', Vehicle_registerListView.as_view(), name='vehicle-list'),
    path('transport/vehicles_details/<int:pk>/', Vehicle_registerDetailView.as_view(), name='vehicle-details'),
    path('transport/vehicles_update/<int:pk>/', Vehicle_registerUpdateView.as_view(), name='vehicle-update'),
    #fuel assign
    path('transport/assign_fuel/', Assign_fuelCreateView.as_view(), name='assign-fuel'),
    #path('transport/fueled_v/', Assign_fuelListView.as_view(), name='fuel-list'),
    #path('transport/fueled_v_details/<int:pk>/', Assign_fueltDetailView.as_view(), name='fuel-details'),
    #fuel requests
    #path('transport/request_fuel/', Request_fuelCreateView.as_view(), name='request-fuel'),
    path('transport/fuel_request_details/<int:pk>/', Request_fueltDetailView.as_view(), name='request-fuel-details'),
    #path('transport/fueled_requests_list/', Request_fuelListView.as_view(), name='request-fuel-list'),
    path('user/<str:username>/', UserRequest_fuelListView.as_view(), name='user-requests'),    
    path('transport/request_approve/<int:pk>/', Request_fuelUpdate.as_view(), name='approve-request'),
    path('transport/<int:pk>/update/', Request_fuel_UpdateView.as_view(), name='request-update'), 
    path('transport/<int:pk>/delete', Request_fuelDeleteView.as_view(), name='request-delete'),
    path('transport/request_approve_complete/<int:pk>/', Request_fuel_completeUpdate.as_view(), name='fuel-request-complete'),
   
    #functionalities
    path('error/', PermissionsView.as_view()),
    path('pdf/<pk>/', fuelapproval_render_pdf_view, name='approval-pdf-view'),
    
    #add vehicles and drivers
    path('transport/add_vehicle/', Vehicle_registerCreateView.as_view(), name='add-vehicle'),
    path('transport/add_driver/', DriverCreateView.as_view(), name='add-driver'),
    path('transport/edit_driver/<int:pk>/', DriverUpdateView.as_view(), name='driver-update'),

    path('transport/request_approve_decline/<int:pk>/', Request_fuel_declineUpdate.as_view(), name='approval-declined'),
    path('index/', views.index),    
    path('transport/v_issues/', Vehicle_issuesCreateView.as_view(), name='vehicle-issues'), 
    path('transport/v_issues_list/', Vehicle_issuesListView.as_view(), name='v-issue-list'),
    path('transport/v_handover/', FormWizardView.as_view(), name='vehicle-handover'),

    #new links for fuel_mgt requests management, to check corresponding templates
    path('transport/new_req/', views.Fuel_mgtCreateView.as_view(), name='new-request'),
    path('transport/request_details/<int:pk>/', Fuel_mgtDetailView.as_view(), name='fuel-details'),
    path('transport/fuelmgt_list/', Fuel_mgtListView.as_view(), name='fuel-mgt-list'),
    path('transport/<int:pk>/request/delete', Fuel_mgtDeleteView.as_view(), name='fuel-request-delete'),
    path('transport/<int:pk>/request/update/', Fuel_mgtUpdateView.as_view(), name='fuel-request-update'),     
    path('transport/<int:pk>/user/update/', Fuel_mgt_UpdateView.as_view(), name='fuel-request-user-update'), 
    path('transport/user/<str:username>/', UserFuel_mgtListView.as_view(), name='user-fuel-request-list'),     
    path('transport/request/approve_decline/<int:pk>/', Fuel_mgt_declineUpdate.as_view(), name='fuel-request-approval-declined'),
    path('transport/request/approve_complete/<int:pk>/', Fuel_mgt_completeUpdate.as_view(), name='fuelmgt-request-complete'),
    
    #new links for fuel_mgt fuel issuance
    path('transport/fuel_assign/<int:pk>/', Fuel_mgt_f_issue_UpdateView.as_view(), name='assign-fuel'),
    path('transport/fueled_vehicles_details/<int:pk>/', Fuel_mgtDetailView.as_view(), name='fuel-details'),

    #mechanic assessment and garage operations
    path('transport/mech_assessment/<int:pk>/', mechanic_assesmentUpdate.as_view(), name='mech-assesment'),
    path('transport/work_assessment/<int:pk>/', work_assessmentUpdateView.as_view(), name='work-assesment'),
    path('transport/work_assessment_approval/<int:pk>/', work_assessment_approvalUpdateView.as_view(), name='work-assesment-approval'),
    path('transport/work_assessment_detail/<int:pk>/', work_assessmentDetailView.as_view(), name='work-assesment-detail'),
    path('transport/mech_assessment/', Vehicle_issuesDetailView.as_view(), name='mech-assesment-detail'),

    #fuel request filters
    path('transport/filter-requests/', views.Reqfilter, name='fuel-request-filter'), 

    #functions for linking fields
    path('ajax/load-prices/', views.load_prices, name='ajax-load-prices'), 
    path('ajax/load-vehicles/', views.load_vehicles, name='ajax-load-vehicles'), 
    path('ajax/load-codes/', views.load_user_regions, name='ajax-load-codes'), 
    path('add/', views.PersonCreateView.as_view(), name='person_add'),   
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-vendor-locations/', views.load_vendor_location, name='ajax-load-vendor-locations'),
    path('ajax/load-vendor-fuel-types/', views.load_vendor_fuel_types, name='load-vendor-fuel-types'),
    path('ajax/load-vendor-prices/', views.load_vendor_prices, name='ajax-load-vendor-prices'),
    path('ajax/load-discounts/', views.load_vendor_discounts, name='ajax-load-discounts'),


    #links for adding and listing driver incidents
    path('transport/driver_incidents/', views.Driver_IncidentsCreateView.as_view(), name='new-driver-incidents'),
    path('transport/driver_incidents_list/', Driver_IncidentsListView.as_view(), name='driver-incidents-list'),
    
    #link to test multiplication of form fields
    path('transport/test_m/', TestMCreateView.as_view(), name='test-mutl'),
    path('maths/', views.total, name='total'),
    path('transport/test_m_list/', TestMListView.as_view(), name='test-list'),

    #link to test new fuel request form
    path('transport/new_req_create/', views.Fuel_mgt_updateCreateView.as_view(), name='new-request-updated'),

    #links for vehicle repair #for continous update...
    path('transport/garage/<int:pk>/', views.mechanic_assesmentUpdate.as_view(), name='mech-assessment'),
    #link for registering motor cycle
    path('transport/motorbikes_create/', views.Motorbike_registerCreateView.as_view(), name='new-bikes'),
    path('transport/motorbikes_list/', views.Motorcycle_ListView.as_view(), name='bikes-list'),
    
    #links for managing riders  
    path('transport/rider_create/', views.Rider_CreateView.as_view(), name='new-rider'), 
    path('transport/riders_list/', views.Rider_ListView.as_view(), name='list-riders'),

    #links for generators 
    path('transport/generator_create/', views.Generator_CreateView.as_view(), name='new-generator'),
    path('transport/generator_list/', views.Generator_ListView.as_view(), name='list-generators'),

    #link for new fuel mgtm forms 
    path('transport/fuel_create/', views.Fuel_mgt_mCreateView.as_view(), name='fuelm-create'),
    path('transport/fuelmgtm_list/', Fuel_mgt_mListView.as_view(), name='fuel-mgtm-list'),
    path('transport/fuelmgtm_details/<int:pk>/', Fuel_mgt_mDetailView.as_view(), name='fuel-mgtm-details'),
    path('transport/fuelmgtm_update/<int:pk>/request/', Fuel_mgt_mUpdateView.as_view(), name='fuel-mgtm-request-update'),
    path('transport/fuelmgtm_update/approve_complete/<int:pk>/', Fuel_mgt_mcompleteUpdate.as_view(), name='fuelmgtm-request-complete'),
    path('transport/delete/<int:pk>/', Fuel_mgtmDeleteView.as_view(), name='fuel-mgtm-delete'),
    path('transport/request/decline/<int:pk>/', Fuel_mgtm_declineUpdate.as_view(), name='fuel-mgtm-declined'),
    path('transport/fuelmgtm_fuel_assign/<int:pk>/', Fuel_mgtm_f_issue_UpdateView.as_view(), name='fuel-mgtm-assign-fuel'),
    path('transport/fuelmgtm_details/<int:pk>/', Fuel_mgtmDetailView.as_view(), name='fuel-mgtm-fuel-details'),
    path('transport/my_fuel_requests/<str:username>/', UserFuel_mgmtListView.as_view(), name='my-fuel-requests-list'), 
    path('transport/request/bpoapprove_complete/<int:pk>/', Fuel_mgt_mBPOUpdateView.as_view(), name='fuelmgt-request-bpoapproval'),
    path('transport/approval_tasks/', views.taskList, name ='tasks'),
    #messaging
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),
    
    #motorbike fuel management
    path('transport/fuel_mb_create/', views.Fuel_mgt_mbikeCreateView.as_view(), name='fuelmb-create'),
    ]

    