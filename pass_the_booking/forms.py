from django import forms
from .models import Client, Property, Booking

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('name', 'dob', 'email', 'telephone',)

class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ('address', 'price', 'bedrooms', 'internet',)

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('guest_name', 'guest_email', 'check_in', 'check_out',)