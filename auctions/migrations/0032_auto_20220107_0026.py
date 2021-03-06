# Generated by Django 3.1 on 2022-01-07 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0031_listing_creator_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='active',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='name',
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='NA', max_length=200, verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='starting_bid',
            field=models.PositiveIntegerField(default=0, verbose_name='starting bid'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='title',
            field=models.CharField(default='Title', max_length=50, verbose_name='title'),
            preserve_default=False,
        ),
    ]
