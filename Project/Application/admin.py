from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Places)
class AdminPlace(admin.ModelAdmin):
        list_display=['id','bookplace']

@admin.register(Booking)
class AdminBook(admin.ModelAdmin):
        list_display=['id','email','traveldate','adults','destination','phone','aadhar',"amount"]

@admin.register(Destinations)
class AdminDestination(admin.ModelAdmin):
    list_display=['id','days','amount','quote','place','image']