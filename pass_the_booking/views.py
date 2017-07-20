from django.shortcuts import render
from .models import Client



def client_list(request):
    clients = Client.objects.order_by('name')
    return render(request, 'pass_the_booking/client_list.html', {'clients': clients})
