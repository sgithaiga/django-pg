# Generated by Django 3.1.2 on 2021-10-06 10:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0007_parts_fitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='parts',
            name='date_fitted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
