# Generated by Django 3.1.2 on 2022-01-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0038_auto_20220114_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='description'),
        ),
    ]