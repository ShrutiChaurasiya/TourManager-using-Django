# Generated by Django 4.2.1 on 2023-07-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('email', models.TextField(max_length=50)),
                ('traveldate', models.DateField(auto_now=True)),
                ('adults', models.TextField(max_length=15)),
                ('phone', models.TextField(max_length=10)),
                ('aadhar', models.TextField(max_length=12, primary_key=True, serialize=False)),
            ],
        ),
    ]
