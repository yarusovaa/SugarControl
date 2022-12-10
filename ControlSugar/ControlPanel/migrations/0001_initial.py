# Generated by Django 4.1.3 on 2022-12-04 18:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Surname', models.TextField()),
                ('Birthday', models.DateField(default=datetime.datetime(2022, 12, 4, 21, 19, 14, 417503))),
                ('Password', models.TextField()),
                ('Login', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BloodMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(default=datetime.datetime(2022, 12, 4, 21, 19, 14, 418072))),
                ('TypeMeasurement', models.BooleanField()),
                ('DataMeasurement', models.FloatField()),
                ('Person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlPanel.person')),
            ],
        ),
    ]