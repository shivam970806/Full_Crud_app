# Generated by Django 3.0.7 on 2021-08-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
                ('mobile', models.CharField(max_length=12)),
                ('country', models.CharField(max_length=12)),
                ('bio', models.CharField(max_length=500)),
            ],
        ),
    ]