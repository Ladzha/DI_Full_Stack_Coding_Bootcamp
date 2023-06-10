# Generated by Django 4.2.1 on 2023-06-10 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_alter_customer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='rental',
            name='rental_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rentalrate',
            name='daily_rate',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rentalstation',
            name='capacity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]