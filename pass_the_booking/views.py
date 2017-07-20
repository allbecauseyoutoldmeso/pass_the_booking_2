from django.shortcuts import render

def client_list(request):
    return render(request, 'pass_the_booking/client_list.html', {})
