# Generated by Django 3.1.2 on 2021-10-25 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0014_auto_20211025_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle_register',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
