# Generated by Django 4.1.3 on 2022-12-04 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodmeasurement',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 4, 21, 19, 17, 646186)),
        ),
        migrations.AlterField(
            model_name='person',
            name='Birthday',
            field=models.DateField(default=datetime.datetime(2022, 12, 4, 21, 19, 17, 645758)),
        ),
    ]