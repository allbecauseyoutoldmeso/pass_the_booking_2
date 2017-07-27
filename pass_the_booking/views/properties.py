from ..models import Client, Property, Booking
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View

class PropertyListView(ListView):
    model = Property
    template_name = 'pass_the_booking/properties/property_list.html'

class PropertyCreate(CreateView):
    model = Property
    fields = ['client', 'address', 'price', 'bedrooms', 'internet']
    template_name = 'pass_the_booking/object_edit.html'

class PropertyUpdate(UpdateView):
    model = Property
    fields = ['client', 'address', 'price', 'bedrooms', 'internet']
    template_name = 'pass_the_booking/object_edit.html'

# class PropertyDetailView(View):
#
#     def get(self, request, pk):
#         property = get_object_or_404(Property, pk=pk)
#         return render(request, 'pass_the_booking/properties/property_detail.html', {'property': property})

class PropertyDetaiView(DetailView):
    model = Property
    template_name = 'pass_the_booking/properties/property_detail.html'
    context_object_name = 'property'

class PropertyDelete(DeleteView):
    model = Property
    template_name = 'pass_the_booking/object_confirm_delete.html'
    success_url = reverse_lazy('property_list')
