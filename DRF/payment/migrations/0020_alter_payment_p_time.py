# Generated by Django 4.1.1 on 2023-01-11 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0019_payment_p_done_alter_payment_p_booking_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='p_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 11, 10, 46, 29, 644374)),
        ),
    ]