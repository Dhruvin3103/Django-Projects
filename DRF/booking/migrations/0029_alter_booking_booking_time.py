# Generated by Django 4.1.1 on 2023-02-12 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0028_alter_booking_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 12, 11, 34, 59, 672804)),
        ),
    ]
