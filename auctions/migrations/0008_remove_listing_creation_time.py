# Generated by Django 3.1 on 2022-01-05 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20220105_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='creation_time',
        ),
    ]
