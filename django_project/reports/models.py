from django.db import models
from django.utils import timezone

# Create your models here.
class Historic_Consumption(models.Model):
    consumption_date = models.DateField(blank=True, null=True, default=timezone.now)
    registration_no = models.CharField(blank=True, null=True, max_length=255)
    region = models.CharField(blank=True, null=True, max_length=255)
    fuel_type = models.CharField(blank=True, null=True, max_length=255)
    quantity = models.FloatField(blank=True, null=True, max_length=255)
    cost_per_liter = models.FloatField()
    total_amount = models.FloatField()

    def __str__(self):
        return self.registration_no
