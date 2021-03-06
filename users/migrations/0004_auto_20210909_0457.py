# Generated by Django 3.2.7 on 2021-09-09 04:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_auto_20210908_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='valid_upto',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 9, 5, 27, 34, 230074)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
