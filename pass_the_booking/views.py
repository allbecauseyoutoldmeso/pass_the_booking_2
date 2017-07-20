from .models import Client, Property, Booking
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClientForm, PropertyForm, BookingForm

def client_list(request):
    clients = Client.objects.order_by('name')
    return render(request, 'pass_the_booking/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    properties = client.property_set.all()
    return render(request, 'pass_the_booking/client_detail.html', {'client': client, 'properties': properties})

def client_new(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
        return render(request, 'pass_the_booking/client_edit.html', {'form': form})

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
        return render(request, 'pass_the_booking/client_edit.html', {'form': form})

def properties(request):
    properties = Property.objects.order_by('client')
    return render(request, 'pass_the_booking/properties.html', {'properties': properties })

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    bookings = property.booking_set.all()
    return render(request, 'pass_the_booking/property_detail.html', {'property': property, 'bookings': bookings })

def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'pass_the_booking/booking_detail.html', {'booking': booking })

def booking_new(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.property = property
            booking.save()
            return redirect('booking_detail', pk=booking.pk)
    else:
        form = BookingForm()
        return render(request, 'pass_the_booking/booking_edit.html', { 'form': form, 'property': property })

def property_new(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.client = client
            property.save()
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm()
        return render(request, 'pass_the_booking/property_edit.html', { 'form': form, 'client': client })
