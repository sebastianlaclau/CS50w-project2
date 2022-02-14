# Generated by Django 4.0.1 on 2022-01-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0047_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('FA', 'Fashion'), ('CE', 'Consumer Electronics'), ('SG', 'Sporting goods'), ('HW', 'Health & Wellness'), ('PS', 'Pets supplies'), ('CG', 'Children’s goods')], max_length=50),
        ),
    ]