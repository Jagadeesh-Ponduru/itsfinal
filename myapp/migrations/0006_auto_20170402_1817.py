# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-02 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20170329_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='Sensor_value',
            field=models.IntegerField(),
        ),
    ]
