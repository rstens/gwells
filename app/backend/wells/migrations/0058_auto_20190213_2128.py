# Generated by Django 2.1.7 on 2019-02-13 21:28

from django.db import migrations


def insert_unk_well_class_code(apps, schema_editor):
    data = {
        'UNK': {
            "description": "Unknown",
            "display_order": 19,
            "effective_date": "2019-02-12 01:00:00Z",
            "expiry_date": "9999-12-31T23:59:59.999999Z",
            "create_user": "ETL_USER",
            "create_date": "2019-02-12 01:00:00Z",
            "update_user": "ETL_USER",
            "update_date": "2019-02-12 01:00:00Z"
        },
    }
    WellClassCode = apps.get_model('wells', 'WellClassCode')

    for (key, value) in data.items():
        WellClassCode.objects.update_or_create(well_class_code=key, defaults=value)


def revert_unk_well_class_code(apps, schema_editor):
    # Deleting these could be dangerous (we don't want to cascade delete the submissions),
    # so we do nothing here.
    logger.warn('Not deleting WellClassCode records! That would be dangerous.')


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0057_auto_20190211_2158'),
    ]

    operations = [
        migrations.RunPython(insert_unk_well_class_code, revert_unk_well_class_code),
    ]
