# Generated by Django 4.2.1 on 2023-06-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='type',
            field=models.CharField(choices=[('SUN', 'sunny'), ('CL', 'cloudy'), ('WIN', 'windy'), ('RAI', 'rainy'), ('ST', 'stormy')], default=1, max_length=5),
            preserve_default=False,
        ),
    ]
