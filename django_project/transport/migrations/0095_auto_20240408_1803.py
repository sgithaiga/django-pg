# Generated by Django 3.1.2 on 2024-04-08 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0094_auto_20240408_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel_mgt_xn',
            name='previous_worksheet',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='fuel_mgt_xn',
            name='site_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
