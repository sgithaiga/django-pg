# Generated by Django 3.1.2 on 2021-10-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0010_auto_20211005_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel_price',
            name='fuel_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
