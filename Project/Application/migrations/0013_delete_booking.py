# Generated by Django 4.2.2 on 2023-07-25 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0012_remove_booking_destination_delete_places'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
