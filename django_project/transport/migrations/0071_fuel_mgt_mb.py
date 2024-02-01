# Generated by Django 3.1.2 on 2023-12-14 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transport', '0070_auto_20230524_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuel_mgt_mb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_reference', models.UUIDField(default=uuid.uuid4)),
                ('fuel_amount_requested', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('date_approved', models.DateTimeField(auto_now=True, null=True)),
                ('fuel_issue_complete', models.BooleanField(default=False)),
                ('date_closed', models.DateTimeField(default=django.utils.timezone.now)),
                ('declined', models.BooleanField(default=False)),
                ('reason', models.TextField(blank=True, null=True)),
                ('barcode', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('previous_liters_served', models.CharField(max_length=100, null=True)),
                ('liters_served', models.IntegerField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('previous_mileage', models.CharField(blank=True, max_length=100, null=True)),
                ('current_mileage', models.CharField(blank=True, max_length=100, null=True)),
                ('distance_covered', models.CharField(max_length=100, null=True)),
                ('date_fueled', models.DateTimeField(default=django.utils.timezone.now)),
                ('station_mileage', models.CharField(blank=True, max_length=100, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('fprice', models.CharField(max_length=100, null=True)),
                ('work_ticket_number', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('BPO_approval', models.BooleanField(default=False)),
                ('date_BPO_approved', models.DateTimeField(auto_now=True, null=True)),
                ('fuel_Img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('approved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('approved_by_BPO', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('assign_request', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('attended_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('closed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('discount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mbdiscountprice', to='transport.vendor_price')),
                ('fuel_station_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='transport.fuel_station')),
                ('fuel_type_requested', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mbfueltype', to='transport.vendor_fuel_types')),
                ('motor_cycle_reg_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='transport.motor_bike_register')),
                ('price_per_liter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mbfuelprice', to='transport.vendor_price')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transport.station')),
                ('region_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='transport.userunit')),
                ('requested_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('rider_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='transport.motor_bike_riders')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transport.vendor')),
                ('vendor_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='transport.vendor_station')),
            ],
        ),
    ]
