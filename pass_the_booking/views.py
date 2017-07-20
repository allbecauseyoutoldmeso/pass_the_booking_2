from .models import Client, Property
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ClientForm

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
    return render(request, 'pass_the_booking/property_detail.html', {'property': property })
