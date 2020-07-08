from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Driver, Booking


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': "Enter your First Name"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': "Enter your Last Name"}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'placeholder': "Enter your Email"}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': "Enter your Username"}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': "Enter Password"}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': "Confirm Password"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', "username", 'email', 'password1', 'password2']


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': "Enter your First Name"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': "Enter your Last Name"}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'placeholder': "Enter your Email"}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': "Enter your Username"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', "username", 'email']


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['current_location', 'license_number', 'vehicle_name', 'vehicle_number', 'image', 'is_available']
        labels = {
            'image': "Profile Image", "vehicle_number": "Vehicle Number",
            "vehicle_name": "Car brand", "license_number": "License Number",
            "current_location": "Current Location", 'is_available': "Available"
        }


class BookingForm(forms.ModelForm):
    full_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': "Enter your Full Name"}))
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'placeholder': "Enter your Email"}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': "Enter your Phone #"}))
    passengers = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': "Enter Number of Passenger"}))
    location = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': "Enter Location"}))
    destination = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': "Enter Destination"}))

    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone', 'passengers', 'destination', 'location']