# Generated by Django 2.2.1 on 2019-05-14 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0085_merge_20190514_0037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linerperforation',
            name='activity_submission',
        ),
    ]