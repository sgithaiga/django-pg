from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from transport.models import Vehicle_register 
# Create your models here.


class SpeedGovernorCompliance(models.Model):
    pass

class NTSACompliance(models.Model):
    registration_no = models.ForeignKey(
        Vehicle_register,
        on_delete=models.CASCADE,
        verbose_name="Vehicle Registration Number"
    )
    inspection_date = models.DateField(verbose_name="Inspection Date")
    next_inspection_date = models.DateField(verbose_name="Next Inspection Date")
    last_inspection_date = models.DateField(auto_now=True, verbose_name="Last Inspection Date")
    inspection_sticker_issued_date = models.DateField(verbose_name="Sticker Issuance Date")
    inspection_sticker_expiry_date = models.DateField(verbose_name="Sticker Expiry Date")
    booking_fee = models.FloatField(verbose_name="Booking Fee")
    inspection_fee = models.FloatField(verbose_name="Inspection Fee")
    total_fees = models.FloatField(null=True, verbose_name="Total Fees")

    def save(self, *args, **kwargs):
        # Calculate the total fees before saving
        self.total_fees = self.booking_fee + self.inspection_fee
        super().save(*args, **kwargs)
    
    def next_inspection_date_formatted(self):
        return self.next_inspection_date.strftime("%Y-%m-%d")    
    
    def __str__(self):
        return f"Compliance for {self.registration_no}"


class InsuranceCompliance(models.Model):
    vehicle = models.ForeignKey(
        Vehicle_register, null=True, 
        on_delete=models.CASCADE,
        verbose_name=_("Vehicle")
    )
    insurance_provider = models.CharField(null=True, 
        max_length=255,
        verbose_name=_("Insurance Provider")
    )
    date_policy_issued = models.DateField(null=True, 
        verbose_name=_("Date Policy Issued")
    )
    date_policy_expiry = models.DateField(null=True, 
        verbose_name=_("Date Policy Expiry")
    )
    insurance_fee = models.FloatField(null=True, 
        verbose_name=_("Insurance Fee")
    )

    class Meta:
        verbose_name = _("Insurance Compliance")
        verbose_name_plural = _("Insurance Compliances")
    
    def date_policy_expiry_formatted(self):
        return self.date_policy_expiry.strftime("%Y-%m-%d")    
    
    def __str__(self):
        return f'{self.vehicle} - {self.insurance_provider} - {self.date_policy_issued} - {self.date_policy_expiry}'
