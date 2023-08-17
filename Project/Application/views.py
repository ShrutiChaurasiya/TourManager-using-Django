from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
# User Related Views
def home(request):
    return render(request,'replica.html')

@login_required(login_url='login')
def home1(request):
    destination_obj= Destinations.objects.all()
    params={
        "destination_obj":destination_obj
    }
    return render(request,'home1.html',params)

def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password1')
        user1 = authenticate(username = username , password = pass1)
        if user1 is not None:
            login(request,user1)
            messages.success(request, f'Successfully {username} Logged in ')
            return redirect('home1')
        else:
            messages.warning(request, f'Login Unsuccessful for {username}')
            return redirect('home1')
    
    return render(request,'login.html')


def register(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1!= password2:
           messages.warning(request, f'Passwords did not match for {username}') 
           return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password1)
            user.save()
            print(username,email,password1)
            messages.success(request, f'User created successfully for {username}')
            return render(request,'login.html')
    return render(request,"register.html")


def log(request):
    logout(request)
    messages.success(request , 'User Logout Successful')
    return redirect('home')

def book(request, id=None):
    place_obj=Places.objects.all()
    d=Destinations.objects.all()
    params={
        "place_obj":place_obj,
        "d":d,
        }
    print(place_obj)
    if request.method == 'POST':
        email=request.POST.get('email')
        traveldate1=request.POST.get('traveldate')
        # traveldate=datetime.strptime(traveldate1, "%Y/%m/%d")
        print(traveldate1)
        phone=request.POST.get('phone')
        aadhar=request.POST.get('aadhar')
        adults=request.POST.get('adults')
        destination=request.POST.get('destination')
        print(destination)
        obj = Places.objects.get(bookplace=destination)
        print(obj)
        if_obj=Places.objects.filter(bookplace=destination).values('id')
        print("Destination object ",if_obj)
        booking_obj=Booking.objects.create(email=email, traveldate=traveldate1, phone=phone,aadhar=aadhar,adults=adults, destination=obj)
        booking_obj.save()
        print('objjjjjjjjjjjj',obj)
        print('adddj',adults)
        amt = Destinations.objects.get(place=destination)
        print(amt.amount)
        print(type(adults))
        params={
            "adults":adults,
            "obj":obj,
            "amt" : amt.amount,
            "total": int(adults)*int(amt.amount),
        }
        print(params,"pppppppppppppppp")
        messages.success(request, f'Booking Done successfully for {phone}')
        return render(request,'tickets.html',params)
    else:
        return render(request,'book.html', params)


def tickets(request):
    
    return render(request,"tickets.html")


# Admin Related Views
def adminn_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password1')
        user1 = authenticate(username = username , password = pass1)
        if user1 is not None:
            admin = authenticate(username = 'admin', password = '123')
            print(admin)
            if user1 == admin:
                login(request,admin)
                messages.success(request, f'Successfully {username} Logged in ')
                return redirect('adminn_homepg')
            else :
                messages.warning(request, f'Login Unsuccessful for Admin :- {username} ')
                return redirect('home')

    return render(request,'adminn_login.html')

@login_required(login_url='adminn_login')
def adminn_homepg(request):
    return render(request,'adminn_homepg.html')

# Destination : 
def destination_model(request):
    dm_obj=Destinations.objects.all()
    params={"dm_obj":dm_obj}
    return render(request,'destination_model.html',params)

def add_destination(request):
    if request.method == 'POST':
        days = request.POST['days']
        amount = request.POST['amount']
        quote = request.POST['quote']
        place = request.POST['place']
        image = request.POST['image']
        if len(amount)>=1 and len(place)>=1:
            add_obj = Destinations.objects.create(days=days, amount=amount, quote=quote, place=place, image=image)
            add_obj.save()
            return redirect('destination_model')
        else:
            return redirect('add_destination')

    return render(request,'add_destination.html')


def update_dest(request,id):
    update_dest_obj = Destinations.objects.get(id= id)

    if request.method == 'POST':
        n_days = request.POST['days']
        n_amount = request.POST['amount']
        n_quote = request.POST['quote']
        n_place = request.POST['place']
        
        
        
        update_dest_obj.days = n_days
        update_dest_obj.amount = n_amount
        update_dest_obj.quote = n_quote
        update_dest_obj.place = n_place
        update_dest_obj.image = update_dest_obj.image
        
        update_dest_obj.save()
        return redirect('destination_model')
    upd=Destinations.objects.get(id = id)
    context = {
        "update_dest_obj":update_dest_obj,
        "upd":upd,
        }

    return render(request,'update_dest.html',context)


def deletee_dest(request,id):
    del_dest = Destinations.objects.get(id = id)
    del_dest.delete()
    return redirect("destination_model")
    

# Places : 
def places_model(request):
    pm_obj=Places.objects.all()
    params={"pm_obj":pm_obj}
    return render(request,'places_model.html',params)

def add_place(request):
    if request.method == 'POST':
        bookplace = request.POST['bookplace']
        
        
        if len(bookplace)>=1:
            blog = Places(bookplace = bookplace)
            blog.save()
            return redirect('places_model')
        else:
            return redirect('add_place')

    return render(request,'add_place.html')

def update_places(request,id):
    update_place_obj = Places.objects.get(id= id)

    if request.method == 'POST':
        n_bookplace = request.POST['bookplace']

        update_place_obj.bookplace = n_bookplace
        
        update_place_obj.save()
        return redirect('places_model')
    upd=Places.objects.get(id = id)
    context = {
        "update_place_obj":update_place_obj,
        "upd":upd,
        }

    return render(request,'update_places.html',context)


def deletee_places(request,id):
    del_place = Places.objects.get(id = id)
    del_place.delete()
    return redirect("places_model")


# Booking : 
def booking_model(request):
    bm_obj=Booking.objects.all()
    params={"bm_obj":bm_obj}
    return render(request,'booking_model.html',params)


def booking_add(request):
    place_obj=Places.objects.all()
    
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        destination = request.POST['destination']
        obj = Places.objects.get(bookplace=destination)
        traveldate = request.POST['traveldate']
        aadhar = request.POST['aadhar']
        adults = request.POST['adults']
        
        if len(email)>=1 and len(aadhar)>=1:
            add_obj = Booking.objects.create(email = email, phone=phone, destination=obj,traveldate=traveldate, aadhar=aadhar, adults=adults)
            add_obj.save()
            return redirect('booking_model')
        else:
            return redirect('booking_add')
  
    params={
    "place_obj":place_obj,
    "obj":obj,
    }
    return render(request,'booking_add.html',params)


def update_book(request,id):
    update_book_obj = Booking.objects.get(id= id)
    ifobj=Places.objects.get(id = id)

    if request.method == 'POST':
        n_email = request.POST['email']
        n_phone = request.POST['phone']
        ifobjdestination = request.POST['destination']
        if_obj=Places.objects.filter(bookplace=ifobjdestination).values('id')
        print("Destination object ",if_obj)
        n_traveldate1 = request.POST['traveldate']
        n_traveldate=datetime.strptime(n_traveldate1, "%Y-%m-%d")
        n_aadhar = request.POST['aadhar']
        n_adults = request.POST['adults']
        
        
        update_book_obj.email = n_email
        update_book_obj.phone = n_phone
        ifobj.bookplace =if_obj
        update_book_obj.traveldate = n_traveldate
        update_book_obj.aadhar = n_aadhar
        update_book_obj.adults = n_adults
        
        update_book_obj.save()
        return redirect('booking_model')
    
    upd=Booking.objects.get(id = id)
    date = update_book_obj.traveldate.strftime("%Y-%m-%d")
    print(date)
    context = {
        "update_book_obj":update_book_obj,
        "upd":upd,
        "date": date
        }
    return render(request,'update_book.html',context)


def dele_book(request,id):
    del_book = Booking.objects.get(id = id)
    del_book.delete()
    return redirect("booking_model")


def maldives(request):
    return render(request,'maldives.html')

def malasiya(request):
    return render(request,'malasiya.html')

def nepal(request):
    return render(request,'nepal.html')

def bangkok(request):
    return render(request,'bangkok.html')

def indonesia(request):
    return render(request,'indonesia.html')

def thankyou(request):
    return render(request,'thankyou.html')