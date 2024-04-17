from django.contrib import admin
from .models import NTSACompliance, InsuranceCompliance
# Register your models here.

admin.site.register(NTSACompliance)
admin.site.register(InsuranceCompliance)