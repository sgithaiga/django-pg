# Generated by Django 3.1.2 on 2024-03-16 09:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20240311_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historic_consumption',
            name='consumption_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
