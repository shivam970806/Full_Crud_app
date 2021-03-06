# Generated by Django 3.0.7 on 2021-08-03 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Engine_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.CharField(max_length=100)),
                ('chasis', models.CharField(max_length=100)),
                ('fuel_type', models.CharField(max_length=100)),
                ('old_vehical_no', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehical_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sap_code', models.CharField(max_length=100)),
                ('ledger_name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('vehical_type', models.CharField(max_length=100)),
                ('base_km', models.CharField(max_length=100)),
                ('rto', models.CharField(max_length=100)),
            ],
        ),
    ]
