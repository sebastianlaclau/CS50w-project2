# Generated by Django 3.1 on 2022-01-05 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20220105_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='creator_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]