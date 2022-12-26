# Generated by Django 4.1.1 on 2022-12-26 05:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.DateTimeField(default=datetime.datetime(2022, 12, 26, 10, 44, 54, 669678))),
                ('b_no_of_tickets', models.IntegerField(default=1)),
                ('booking_price', models.IntegerField(default=100)),
                ('movie_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
    ]
