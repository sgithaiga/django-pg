# Generated by Django 3.1.2 on 2024-04-08 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0091_auto_20240408_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel_mgt_xn',
            name='driver_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='transport.driver'),
        ),
        migrations.AlterField(
            model_name='fuel_mgt_xn',
            name='registration_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='transport.vehicle_register'),
        ),
    ]
