# Generated by Django 3.1.2 on 2024-04-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0028_auto_20240414_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imprestpartsaquisition',
            name='date_approved',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='imprestpartsaquisition',
            name='date_requested',
            field=models.DateField(auto_now_add=True),
        ),
    ]
