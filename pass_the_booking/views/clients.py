from ..models import Client
from django.shortcuts import render, get_object_or_404, redirect
from ..forms import ClientForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ClientCreate(CreateView):
    model = Client
    # fields = ['name', 'email', 'dob', 'telephone']
    template_name = 'pass_the_booking/clients/client_edit.html'
    form_class = ClientForm

class ClientUpdate(UpdateView):
    model = Client
    fields = ['name', 'email', 'dob', 'telephone']
    template_name = 'pass_the_booking/clients/client_edit.html'

class ClientDelete(DeleteView):
    model = Client
    template_name = 'pass_the_booking/clients/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')

class ClientListView(ListView):
    model = Client
    template_name = 'pass_the_booking/clients/client_list.html'

class ClientDetailView(View):
    def get(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        properties = client.property_set.all()
        return render(request, 'pass_the_booking/clients/client_detail.html', {'client': client, 'properties': properties})
