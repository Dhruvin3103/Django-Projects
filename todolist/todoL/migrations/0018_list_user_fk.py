# Generated by Django 4.1.1 on 2022-11-07 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoL', '0017_alter_user_imgs'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='user_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]