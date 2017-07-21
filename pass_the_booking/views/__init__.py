from ..models import Client, Property, Booking
from django.shortcuts import render, get_object_or_404, redirect
from ..forms import ClientForm, PropertyForm, BookingForm

from .clients import *
from .properties import *
from .bookings import *

def home_page(request):
    return render(request, 'pass_the_booking/home_page.html')
