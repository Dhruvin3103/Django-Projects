# Generated by Django 4.1.1 on 2023-01-03 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0012_alter_payment_p_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='p_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 3, 11, 35, 13, 116627)),
        ),
    ]
