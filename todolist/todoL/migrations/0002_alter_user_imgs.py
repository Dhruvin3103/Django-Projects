# Generated by Django 4.1.1 on 2022-10-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoL', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='imgs',
            field=models.ImageField(height_field=100, upload_to='image/', width_field=100),
        ),
    ]