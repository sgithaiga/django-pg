# Generated by Django 3.1.2 on 2023-05-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0065_motor_bike_assignment_register_motor_bike_riders'),
    ]

    operations = [
        migrations.AddField(
            model_name='motor_bike_riders',
            name='pf_no',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
