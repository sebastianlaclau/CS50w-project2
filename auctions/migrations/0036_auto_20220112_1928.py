# Generated by Django 3.1 on 2022-01-12 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0035_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='listinng',
            new_name='listing',
        ),
    ]
