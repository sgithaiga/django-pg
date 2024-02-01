from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from transport.models import Vehicle_register

# Create your models here.
class Vehicle(models.Model):

    registration_number = models.ForeignKey(Vehicle_register, on_delete=models.CASCADE, null = True)
    date_ordered = models.DateTimeField(default=timezone.now)
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    order = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('parts:vehicle_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.registration_number.registration_no

class Parts(models.Model):

    title = models.CharField(null=False, blank=False, max_length=255)
    Vehicle = models.ForeignKey('Vehicle', null=False, blank=False,
                            on_delete=models.CASCADE, related_name='vehicle_part')
    quantity = models.CharField(null=True, blank=False, max_length=255)
    delivered = models.BooleanField(default=False)
    date_delivered = models.DateTimeField(default=timezone.now)
    fitted = models.BooleanField(default=False)
    date_fitted = models.DateTimeField(default=timezone.now)
