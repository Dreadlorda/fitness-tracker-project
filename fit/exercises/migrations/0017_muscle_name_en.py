# Generated by Django 3.2.13 on 2022-05-10 10:07
# Edited by Tom on 2022-05-12 18:30 to include name_en values

from django.db import migrations, models

# Will also set the name_en value in the migration
muscle_names = [
    (1, 'Biceps'),
    (2, 'Shoulders'),
    (4, 'Chest'),
    (5, 'Triceps'),
    (6, 'Abs'),
    (7, 'Calves'),
    (8, 'Glutes'),
    (10, 'Quads'),
    (11, 'Hamstrings'),
    (12, 'Lats'),
    (16, 'Lower back'),
]


def set_names(apps, schema_editor):
    Muscle = apps.get_model('exercises', 'Muscle')
    for mapping in muscle_names:
        try:
            m = Muscle.objects.get(pk=mapping[0])
            m.name_en = mapping[1]
            m.save()
        except Muscle.DoesNotExist:
            pass


class Migration(migrations.Migration):
    dependencies = [
        ('exercises', '0016_exercisealias'),
    ]

    operations = [
        migrations.AddField(
            model_name='muscle',
            name='name_en',
            field=models.CharField(
                default='',
                help_text='A more basic name for the muscle',
                max_length=50,
                verbose_name='Alternative name',
            ),
        ),
        migrations.RunPython(set_names),
    ]
