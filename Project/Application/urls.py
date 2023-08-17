from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    # replica.html is in the home view 

    # User related urls.
    path('home1',views.home1,name='home1'),
    path('login/',views.login1,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.log,name='logout'),
    path('book/',views.book,name='book'),
    path('tickets/',views.tickets,name='tickets'),
    path('malasiya/',views.malasiya,name='malasiya'),
    path('nepal/',views.nepal,name='nepal'),
    path('maldives/',views.maldives,name='maldives'),
    path('bangkok/',views.bangkok,name='bangkok'),
    path('indonesia/',views.indonesia,name='indonesia'),    
    path('thankyou/',views.thankyou,name='thankyou'),
    # Admin URLs

    # 1. Admin home Page Urls
    path('adminn_homepg/', views.adminn_homepg,name='adminn_homepg'),

    # Admin Login and Registeration
    path('adminn_login/', views.adminn_login,name='adminn_login'),

    # 2. Destination Models Urls
    path('destination_model/', views.destination_model,name='destination_model'),
    path('add_destination/', views.add_destination,name='add_destination'),
    path('destination_update/<int:id>', views.update_dest,name='update_dest'),
    path('destination_delete/<int:id>', views.deletee_dest,name='deletee_dest'),

    # 3. Places Model Urls
    path('places_model/', views.places_model,name='places_model'),
    path('add_place/', views.add_place,name='add_place'),
    path('update_places/<int:id>', views.update_places,name='update_places'),
    path('deletee_places/<int:id>', views.deletee_places,name='deletee_places'),

    # 4. Booking models Urls
    path('booking_model/', views.booking_model,name='booking_model'),
    path('dele_book/<int:id>', views.dele_book,name='dele_book'),
    path('update_book/<int:id>', views.update_book,name='update_book'),
    path('booking_add/', views.booking_add,name='booking_add'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


