# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-03 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollution', '0002_auto_20180502_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='pH',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='sensor',
            name='water_flow',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='turbidity_value',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='water',
            field=models.FloatField(default=0),
        ),
    ]
