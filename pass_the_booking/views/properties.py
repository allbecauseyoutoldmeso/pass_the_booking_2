from ..models import Client, Property, Booking
from django.shortcuts import render, get_object_or_404, redirect
from ..forms import ClientForm, PropertyForm, BookingForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PropertyListView(ListView):
    model = Property
    template_name = 'pass_the_booking/properties/property_list.html'

def property_list(request):
    properties = Property.objects.order_by('client')
    return render(request, 'pass_the_booking/properties/property_list.html', {'properties': properties })

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    bookings = property.booking_set.all()
    return render(request, 'pass_the_booking/properties/property_detail.html', {'property': property, 'bookings': bookings })

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
    return render(request, 'pass_the_booking/properties/property_edit.html', { 'form': form, 'client': client })

def property_edit(request, pk):
    property = get_object_or_404(Property, pk=pk)
    client = property.client
    if request.method == "POST":
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            property = form.save(commit=True)
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm(instance=property)
    return render(request, 'pass_the_booking/properties/property_edit.html', {'form': form, 'client': client })

def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    client = property.client
    property.delete()
    return redirect('client_detail', pk=client.pk)
