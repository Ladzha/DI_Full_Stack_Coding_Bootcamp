# Generated by Django 4.2.1 on 2023-06-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_alter_address_address2_alter_rental_rental_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.CharField(blank=True, default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rentalstation',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vehiclesize',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]