# Generated by Django 4.2.1 on 2023-06-12 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0003_forecaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='forecaster',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='weatherapp.forecaster'),
            preserve_default=False,
        ),
    ]
