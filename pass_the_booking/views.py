from django.shortcuts import render
from .models import Client
from django.shortcuts import render, get_object_or_404

def client_list(request):
    clients = Client.objects.order_by('name')
    return render(request, 'pass_the_booking/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'pass_the_booking/client_detail.html', {'client': client})
