# Generated by Django 2.2.7 on 2019-11-29 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0007_auto_20191128_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_sighting',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
