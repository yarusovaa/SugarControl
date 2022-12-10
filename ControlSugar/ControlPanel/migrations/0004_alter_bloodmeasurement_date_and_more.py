# Generated by Django 4.1.3 on 2022-12-04 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPanel', '0003_alter_bloodmeasurement_date_alter_person_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodmeasurement',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 12, 5)),
        ),
        migrations.AlterField(
            model_name='bloodmeasurement',
            name='TypeMeasurement',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='Birthday',
            field=models.DateField(default=datetime.datetime(2022, 12, 5, 1, 6, 35, 141717)),
        ),
    ]
