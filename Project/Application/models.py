from django.db import models
from django.core.validators import *
# Create your models here.

class Places(models.Model):
    bookplace=models.CharField(max_length=20)
    def __str__(self):
        return self.bookplace


class Booking(models.Model):
    email=models.TextField(max_length=50)
    traveldate=models.DateField()
    # auto_now=True
    adults=models.TextField(max_length=15)
    phone=models.TextField(validators = [MinLengthValidator(10), MaxLengthValidator(10)], max_length = 10)
    aadhar=models.TextField(validators = [MinLengthValidator(12), MaxLengthValidator(12)], max_length =12)
    amount=models.TextField(max_length=1000000)
    destination=models.ForeignKey(Places,on_delete=models.CASCADE)

    def __str__(self):
        return 'Email:-'+self.email
    

class Destinations(models.Model):
    days=models.TextField(max_length=10)
    amount=models.TextField(max_length=15)
    quote=models.TextField(max_length=100)
    place=models.TextField(max_length=50)
    image=models.ImageField(upload_to='images/',default='')

    def __str__(self):
        return 'Destination:-'+self.place



