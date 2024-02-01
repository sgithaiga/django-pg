# Generated by Django 3.1.2 on 2022-09-04 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transport', '0034_auto_20220903_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuel_mgt',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transport.vendor'),
        ),
        migrations.AddField(
            model_name='fuel_mgt',
            name='vendor_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transport.vendor_station'),
        ),
        migrations.AddField(
            model_name='fuel_mgt_m',
            name='current_mileage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fuel_mgt_m',
            name='distance_covered',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fuel_mgt_m',
            name='previous_liters_served',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fuel_mgt_m',
            name='previous_mileage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fuel_mgt_m',
            name='station_mileage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='fuel_mgt',
            name='approved_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fapprover1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fuel_mgt',
            name='attended_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fattendant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fuel_mgt',
            name='closed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ffueler1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fuel_mgt',
            name='fuel_type_requested',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fueltyper', to='transport.vendor_fuel_types'),
        ),
        migrations.AlterField(
            model_name='fuel_mgt',
            name='price_per_liter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vfuelprice', to='transport.vendor_price'),
        ),
        migrations.AlterField(
            model_name='fuel_mgt',
            name='region_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frcode', to='transport.userunit'),
        ),
        migrations.AlterField(
            model_name='fuel_mgt',
            name='requested_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frequester1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fuel_mgt_m',
            name='approved_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approver1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fuel_mgt_m',
            name='attended_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fuel_mgt_m',
            name='closed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fueler1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fuel_mgt_m',
            name='region_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rcode', to='transport.userunit'),
        ),
        migrations.AlterField(
            model_name='fuel_mgt_m',
            name='requested_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requester1', to=settings.AUTH_USER_MODEL),
        ),
    ]
