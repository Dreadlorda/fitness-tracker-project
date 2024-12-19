# Generated by Django 3.2.15 on 2022-08-25 17:25

from django.db import migrations
from django.conf import settings


def delete_pending_bases(apps, schema_editor):
    """
    Delete all pending bases

    Note that we can't access STATUS_PENDING here because we are not using
    a real model.
    """
    Base = apps.get_model('exercises', 'ExerciseBase')
    Base.objects.filter(status='1').delete()


def delete_pending_translations(apps, schema_editor):
    """
    Delete all pending translations

    Note that we can't access STATUS_PENDING here because we are not using
    a real model.
    """
    Exercise = apps.get_model('exercises', 'Exercise')
    Exercise.objects.filter(status='1').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0014_merge_20210818_1735'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercises', '0017_muscle_name_en'),
    ]

    operations = [
        migrations.RunPython(delete_pending_bases),
        migrations.RunPython(delete_pending_translations),
    ]
