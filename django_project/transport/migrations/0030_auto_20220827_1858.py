# Generated by Django 3.1.2 on 2022-08-27 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0029_auto_20220827_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor_fuel_types',
            name='fuel_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transport.fuel_name'),
        ),
    ]
