# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-22 01:45
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0034_auto_20171121_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productiondata',
            name='yield_estimation_duration',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Estimation Duration'),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='yield_estimation_method',
            field=models.ForeignKey(blank=True, db_column='yield_estimation_method_guid', null=True, on_delete=django.db.models.deletion.CASCADE, to='gwells.YieldEstimationMethod', verbose_name='Estimation Method'),
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='yield_estimation_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Estimation Rate'),
        ),
        migrations.AlterField(
            model_name='well',
            name='well_cap_type',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Well Cap'),
        ),
    ]