# Generated by Django 4.2.1 on 2023-07-21 18:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0010_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='aadhar',
            field=models.TextField(max_length=12, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(12), django.core.validators.MaxLengthValidator(12)]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.TextField(max_length=10, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)]),
        ),
    ]
