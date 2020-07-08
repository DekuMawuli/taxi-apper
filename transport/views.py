from django.shortcuts import render, redirect
from .forms import UserRegisterForm, DriverForm, UserForm, BookingForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Driver, Booking
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect("transport:driver_dashboard")
    # select all drivers and select 3
    drivers = Driver.objects.all()[:3]
    context = {
        "drivers": drivers
    }
    return render(request, 'transport/home.html', context)


def all_drivers(request):
    return render(request, 'transport/driver.html')


def select_driver(request):
    drivers = Driver.objects.all()
    context = {
        "drivers": drivers
    }
    return render(request, 'transport/driver.html', context)


def book_driver(request, pk):
    context = {}
    # select a driver based on the id passed in the url
    driver = Driver.objects.get(user_id__exact=pk)
    if driver is not None:
        context["driver"] = driver
    return render(request, 'transport/book-ride.html', context)


def about(request):
    return render(request, 'transport/about.html')


def contact(request):
    return render(request, 'transport/contact.html')


def driver_login(request):
    return render(request, 'transport/driver-login.html')


def driver_register(request):
    form = UserRegisterForm()
    return render(request, 'transport/driver-register.html', {'form': form})


# the logic used in saving a user into the database
def process_registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully !")
            return redirect("transport:login_driver")
        else:
            messages.error(request, "Password does not match. Please check it again")
            return redirect("transport:register_driver")


@login_required(login_url="transport:login_driver")
def driver_profile(request):
    u_form = UserForm(instance=request.user)
    driver_form = DriverForm(instance=request.user.driver)
    context = {
        "user_form": u_form,
        "driver_form": driver_form
    }
    return render(request, 'transport/driver-profile.html', context)


@login_required(login_url="transport:login_driver")
def update_profile(request):
    if request.method == "POST":
        u_form = UserForm(request.POST, instance=request.user)
        driver_form = DriverForm(request.POST, request.FILES, instance=request.user.driver)
        if u_form.is_valid() and driver_form.is_valid():
            u_form.save()
            driver_form.save()
            messages.success(request, "profile updated")
            return redirect("transport:driver_profile")
        else:
            messages.error(request, "profile couldn't be updated")
            return redirect("transport:driver_profile")


@login_required(login_url="transport:driver_login")
def driver_dashboard(request):
    pending_bookings = Booking.objects.filter(driver__user=request.user).filter(status="P")
    completed_rides = Booking.objects.filter(driver__user=request.user).filter(status="A")
    rejected_rides = Booking.objects.filter(driver__user=request.user).filter(status="R")
    context = {
        'pending_bookings': pending_bookings,
        'completed_bookings': completed_rides,
        'rejected_bookings': rejected_rides,
    }
    return render(request, 'transport/driver_dashboard.html', context)


# the logic used in logging in a user into the database
def process_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = authenticate(request, username=username, password=password)
        except Exception as e:
            messages.error(request, "Invalid Username or Password... Please try again")
            return redirect("transport:login_driver")

        if user is not None:
            login(request, user=user)
            return redirect("transport:driver_dashboard")
        else:
            messages.error(request, "Invalid Username or Password... Please try again")
            return redirect("transport:login_driver")

    else:
        return redirect("transport:login_driver")


# the logic used to add a booking and adding a rider
def booking_ride_process(request, pk):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        passengers = request.POST['passengers']
        location = request.POST['location']
        destination = request.POST['destination']
        booking = Booking(
            full_name=name, email=email,
            phone=phone, passengers=passengers,
            location=location, destination=destination,
            driver_id=pk
        )
        try:
            booking.save()
            messages.success(request, "Booking Completed")
            return redirect("transport:book_ride", pk)
        except Exception as e:
            messages.error(request, e)
            return redirect("transport:book_ride", pk)
    else:
        return redirect("transport:book_ride", pk)


# the logic used in logging out a user
def driver_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("transport:landing_page")


# THIS FUNCTION ALLOW THE DRIVER TO ACCEPT OR REJECT A RIDE REQUEST
# AND BASED ON THAT HIS OR HER AVAILABILITY IS TOGGLED TO EITHER AVAILABLE OR NOT
@login_required(login_url="transport:driver_login")
def approve_ride(request, pk):
    if request.method == "POST":
        status = request.POST['rideStatus']
        booking = Booking.objects.get(id=pk)
        driver = Driver.objects.get(user_id__exact=request.user.id)
        if status == "approve":
            try:
                booking.status = "A"
                booking.save()
                driver.is_available = False
                driver.save()
                messages.success(request, "Ride Accepted")
                return redirect("transport:driver_dashboard")
            except Exception as e:
                messages.success(request, e)
                return redirect("transport:driver_dashboard")
        else:
            try:
                booking.status = "R"
                booking.save()
                messages.success(request, "Ride Rejected")
                return redirect("transport:driver_dashboard")
            except Exception as e:
                messages.success(request, e)
                return redirect("transport:driver_dashboard")
    else:
        return redirect("transport:driver_dashboard")
