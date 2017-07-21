from .clients import *
from .properties import *
from .bookings import *

def home_page(request):
    return render(request, 'pass_the_booking/home_page.html')
