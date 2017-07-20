from django.contrib import admin

from .models import Client
admin.site.register(Client)

from .models import Property
admin.site.register(Property)
