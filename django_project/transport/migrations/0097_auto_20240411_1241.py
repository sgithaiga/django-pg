# Generated by Django 3.1.2 on 2024-04-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0096_auto_20240411_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generator',
            name='serial_number',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
