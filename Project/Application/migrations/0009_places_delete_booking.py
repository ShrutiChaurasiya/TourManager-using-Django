# Generated by Django 4.2.2 on 2023-07-21 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0008_alter_booking_traveldate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookplace', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
