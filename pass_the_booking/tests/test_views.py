from django.test import TestCase
from ..models import Client, Property, Booking

class ViewTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'welcome to pass the booking')

    def test_client_list(self):
        Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')
        response = self.client.get('/clients/')
        self.assertContains(response, 'kate gleeson')

    def test_client_detail(self):
        kate = Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')
        response = self.client.get('/clients/1/')
        self.assertContains(response, 'kate gleeson')

    def test_property_list(self):
        kate = Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')
        Property.objects.create(client = kate, address='123 langthorne road', price=29, bedrooms=2, internet=False)
        response = self.client.get('/properties/')
        self.assertContains(response, '123 langthorne road')

    def test_property_detail(self):
        kate = Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')
        Property.objects.create(client = kate, address='123 langthorne road', price=29, bedrooms=2, internet=False)
        response = self.client.get('/properties/1/')
        self.assertContains(response, '123 langthorne road')

    def test_booking_list(self):
        kate = Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')
        langthorne_road = Property.objects.create(client = kate, address='123 langthorne road', price=29, bedrooms=2, internet=False)
        Booking.objects.create(property = langthorne_road, check_in = '2017-10-12', check_out = '2017-10-14', guest_name = 'sally', guest_email = 'sally@sally.com')
        response = self.client.get('/bookings/')
        self.assertContains(response, "sally's booking for 123 langthorne road")

    def test_booking_detail(self):
        kate = Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')
        langthorne_road = Property.objects.create(client = kate, address='123 langthorne road', price=29, bedrooms=2, internet=False)
        Booking.objects.create(property = langthorne_road, check_in = '2017-10-12', check_out = '2017-10-14', guest_name = 'sally', guest_email = 'sally@sally.com')
        response = self.client.get('/bookings/1/')
        self.assertContains(response, '123 langthorne road')
        self.assertContains(response, 'guest: sally')
