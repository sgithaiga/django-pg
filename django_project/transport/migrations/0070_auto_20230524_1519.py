# Generated by Django 3.1.2 on 2023-05-24 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0069_auto_20230524_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motor_bike_register',
            name='engine_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
