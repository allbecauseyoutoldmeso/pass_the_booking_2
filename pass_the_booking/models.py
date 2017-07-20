from django.db import models
import datetime
from datetime import timedelta

class Client(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    dob = models.DateField()
    telephone = models.CharField(max_length=200)

class Property(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    internet = models.BooleanField()

    def unavailable_dates(self):
        booked_dates = []
        for booking in self.booking_set.all():
            delta = booking.check_out - booking.check_in
            for i in range(delta.days):
                booked_dates.append(booking.check_in + timedelta(i))
        return booked_dates

class Booking(models.Model):

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField(max_length=254)

    def total_price(self):
        return (self.check_out - self.check_in).days * self.property.price
