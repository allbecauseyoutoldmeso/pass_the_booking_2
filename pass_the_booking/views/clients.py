from ..models import Client, Property, Booking
from django.shortcuts import render, get_object_or_404, redirect
from ..forms import ClientForm, PropertyForm, BookingForm

def client_list(request):
    clients = Client.objects.order_by('name')
    return render(request, 'pass_the_booking/clients/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    properties = client.property_set.all()
    return render(request, 'pass_the_booking/clients/client_detail.html', {'client': client, 'properties': properties})

def client_new(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
        return render(request, 'pass_the_booking/clients/client_edit.html', {'form': form})

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=True)
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'pass_the_booking/clients/client_edit.html', {'form': form})

def client_delete(request, pk):
    client = client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('client_list')
