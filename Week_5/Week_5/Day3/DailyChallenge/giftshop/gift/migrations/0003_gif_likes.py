# Generated by Django 4.2.1 on 2023-06-04 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0002_rename_gifts_category_gifs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gif',
            name='likes',
            field=models.IntegerField(default=1),
        ),
    ]
