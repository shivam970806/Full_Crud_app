# Generated by Django 3.0.7 on 2021-08-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_auto_20210811_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
