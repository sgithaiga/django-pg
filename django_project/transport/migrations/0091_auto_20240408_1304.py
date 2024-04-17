# Generated by Django 3.1.2 on 2024-04-08 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0090_auto_20240408_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel_mgt_xn',
            name='driver_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='transport.driver'),
        ),
        migrations.AlterField(
            model_name='fuel_mgt_xn',
            name='registration_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='transport.vehicle_register'),
        ),
    ]
