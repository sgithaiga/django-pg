# Generated by Django 3.1.2 on 2023-05-16 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transport', '0060_auto_20230416_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motor_bike_make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motor_bike_make', models.CharField(choices=[('Suzuki', 'Suzuki'), ('Yamaha', 'Yamaha')], default='Suzuki', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Motor_bike_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motor_cycle_reg_no', models.CharField(max_length=100, null=True, unique=True)),
                ('date_registered', models.DateTimeField(auto_now=True, null=True)),
                ('engine_no', models.CharField(max_length=100, null=True)),
                ('tank_capacity', models.CharField(max_length=100, null=True)),
                ('entered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fuel_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transport.fuel_name')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transport.station')),
            ],
        ),
        migrations.CreateModel(
            name='Motor_bike_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Motor_cycle_model', models.CharField(choices=[('dt125', 'dt125'), ('tf125', 'tf125')], default='dt125', max_length=200)),
                ('motor_cycle_make', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transport.motor_cycle_make')),
            ],
        ),
    ]
