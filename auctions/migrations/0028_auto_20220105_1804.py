# Generated by Django 3.1 on 2022-01-05 18:04

import auctions.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_auto_20220105_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='creator_user',
            field=models.ForeignKey(default=auctions.models.User, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
