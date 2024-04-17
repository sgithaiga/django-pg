from django.urls import path
from .views import (NTSAComplianceCreateView, 
                    NTSAComplianceListView, 
                    InsuranceComplianceCreateView, 
                    InsuranceComplianceListView,
                    NTSAComplianceUpdateView, 
                    InsuranceComplianceUpdateView)

urlpatterns = [
    path('book_inspection/', NTSAComplianceCreateView.as_view(), name='ntsa-compliance-create'),
    path('ntsa_compliance_list/', NTSAComplianceListView.as_view(), name='ntsa-compliance-list'),
    path('insurance/', InsuranceComplianceCreateView.as_view(), name='insurance-compliance-create'),
    path('insurance_compliance_list/', InsuranceComplianceListView.as_view(), name='insurance-compliance-list'),
    path('ntsa_compliance_update/<int:pk>/', NTSAComplianceUpdateView.as_view(), name='ntsa-compliance-update'),
    path('insurance_compliance_update/<int:pk>/', InsuranceComplianceUpdateView.as_view(), name='insurance-compliance-update'),
]
