from ..models import Client, Property, Booking
from django.shortcuts import render, get_object_or_404, redirect
from ..forms import ClientForm, PropertyForm, BookingForm
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View

class BookingListView(ListView):
    model = Booking
    template_name = 'pass_the_booking/bookings/booking_list.html'

class BookingCreate(CreateView):
    model = Booking
    fields = ['property', 'guest_name', 'guest_email', 'check_in', 'check_out']
    template_name = 'pass_the_booking/object_edit.html'

class BookingUpdate(UpdateView):
    model = Booking
    fields = ['property', 'guest_name', 'guest_email', 'check_in', 'check_out']
    template_name = 'pass_the_booking/object_edit.html'




def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'pass_the_booking/bookings/booking_detail.html', {'booking': booking })

def booking_new(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.property = property
            for date in booking.all_dates():
                if date in property.unavailable_dates():
                    messages.add_message(request, messages.INFO, 'Some of the dates you selected are not available.')
                    return redirect('booking_new', pk=property.pk)
            booking.save()
            return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm()
    return render(request, 'pass_the_booking/bookings/booking_edit.html', { 'form': form, 'property': property })

def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    property = booking.property
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=True)
            return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'pass_the_booking/bookings/booking_edit.html', {'form': form, 'property': property })

def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    property = booking.property
    booking.delete()
    return redirect('property_detail', pk=property.pk)
