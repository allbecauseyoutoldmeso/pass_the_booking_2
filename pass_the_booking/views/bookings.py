from ..models import Client, Property, Booking
from django.shortcuts import render, get_object_or_404, redirect
from ..forms import BookingForm
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
    form_class = BookingForm
    template_name = 'pass_the_booking/object_edit.html'

class BookingUpdate(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'pass_the_booking/object_edit.html'

class BookingDetailView(View):
    def get(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        return render(request, 'pass_the_booking/bookings/booking_detail.html', {'booking': booking })

class BookingDelete(DeleteView):
    model = Booking
    template_name = 'pass_the_booking/object_confirm_delete.html'
    success_url = reverse_lazy('booking_list')
