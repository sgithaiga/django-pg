# Generated by Django 3.1.2 on 2021-10-05 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0006_auto_20211002_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel_mgt',
            name='liters_served',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
