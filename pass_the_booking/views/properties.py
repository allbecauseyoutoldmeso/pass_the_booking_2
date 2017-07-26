from ..models import Client, Property, Booking
from django.shortcuts import render, get_object_or_404, redirect
from ..forms import ClientForm, PropertyForm, BookingForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View

class PropertyListView(ListView):
    model = Property
    template_name = 'pass_the_booking/properties/property_list.html'

class PropertyCreate(CreateView):
    model = Property
    fields = ['client', 'address', 'price', 'bedrooms', 'internet']
    template_name = 'pass_the_booking/properties/property_edit.html'

class PropertyUpdate(UpdateView):
    model = Property
    fields = ['client', 'address', 'price', 'bedrooms', 'internet']
    template_name = 'pass_the_booking/properties/property_edit.html'

class PropertyDetailView(View):
    def get(self, request, pk):
        property = get_object_or_404(Property, pk=pk)
        bookings = property.booking_set.all()
        return render(request, 'pass_the_booking/properties/property_detail.html', {'property': property, 'bookings': bookings })

class PropertyDelete(DeleteView):
    model = Property
    template_name = 'pass_the_booking/properties/property_confirm_delete.html'
    success_url = reverse_lazy('property_list')



def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk)
    client = property.client
    property.delete()
    return redirect('client_detail', pk=client.pk)
