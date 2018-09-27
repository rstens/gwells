# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-11 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0008_waterqualitycolour'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitysubmission',
            name='ems_id',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='well',
            name='ems_id',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]