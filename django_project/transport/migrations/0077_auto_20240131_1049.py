# Generated by Django 3.1.2 on 2024-01-31 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0076_fuel_mgt_xn_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
