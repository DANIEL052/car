# Generated by Django 4.1.6 on 2023-02-13 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app_car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='car_owner', to='my_app_car.person'),
        ),
    ]
