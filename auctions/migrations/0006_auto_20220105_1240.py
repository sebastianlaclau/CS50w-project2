# Generated by Django 3.1 on 2022-01-05 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20220105_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='active',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='creation_time',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='creator_user',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='update_time',
        ),
    ]
