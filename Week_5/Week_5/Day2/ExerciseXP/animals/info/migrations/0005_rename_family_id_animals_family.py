# Generated by Django 4.2.1 on 2023-05-30 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_rename_family_animals_family_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animals',
            old_name='family_id',
            new_name='family',
        ),
    ]
