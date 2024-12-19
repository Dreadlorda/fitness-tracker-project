# Generated by Django 3.1.7 on 2021-03-27 11:19

from django.db import migrations, models
import uuid


def generate_uuids(apps, schema_editor):
    """Generate new UUIDs for each exercise image"""

    ExcerciseImage = apps.get_model('exercises', 'ExerciseImage')
    for exercise in ExcerciseImage.objects.all():
        exercise.uuid = uuid.uuid4()
        exercise.save()


class Migration(migrations.Migration):
    dependencies = [
        ('exercises', '0011_auto_20201214_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciseimage',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID'),
        ),
        migrations.RunPython(generate_uuids),
    ]
