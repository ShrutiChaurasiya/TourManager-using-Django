# Generated by Django 4.2.2 on 2023-07-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0007_alter_destinations_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='traveldate',
            field=models.DateField(),
        ),
    ]