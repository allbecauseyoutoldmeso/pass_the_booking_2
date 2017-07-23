from django.db import models
import datetime
from datetime import timedelta
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

class Client(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique = True)
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
            for i in range((booking.check_out - booking.check_in).days):
                d = booking.check_in + timedelta(i)
                booked_dates.append(d.strftime('%Y%m%d'))
        return booked_dates

class Booking(models.Model):

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField(max_length=254)

    def total_price(self):
        return (self.check_out - self.check_in).days * self.property.price

    def all_dates(self):
        dates = []
        for i in range((self.check_out - self.check_in).days):
            d = self.check_in + timedelta(i)
            dates.append(d.strftime('%Y%m%d'))
        return dates

    def clean(self):
        if self.check_in is not None and self.check_out is not None:
            if self.check_in > self.check_out:
                raise ValidationError({'check_out': ('check out cannot be earlier than check in.')})
            if self.check_in < datetime.date.today():
                raise ValidationError({'check_in': ('check in cannot be earlier than today.')})
