# Generated by Django 3.0.7 on 2021-08-26 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0022_auto_20210818_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
