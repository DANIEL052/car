# Generated by Django 4.1.6 on 2023-02-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app_car', '0004_alter_car_renters_alter_rent_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rent',
            name='start_date',
            field=models.DateField(),
        ),
    ]
