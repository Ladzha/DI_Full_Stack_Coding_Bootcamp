# Generated by Django 4.2.1 on 2023-05-29 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_animals_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animals',
            old_name='family',
            new_name='family_id',
        ),
    ]
