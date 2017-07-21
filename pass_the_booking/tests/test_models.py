from django.test import TestCase
from ..models import Client, Property, Booking
import datetime


class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')

    def test_client_has_relevant_details(self):
        """Clients are stored with relevant information"""
        kate = Client.objects.get(name='kate gleeson')
        self.assertEqual(kate.dob, datetime.date(1981, 9, 13))
        self.assertEqual(kate.email, 'kate@kate.com')
        self.assertEqual(kate.telephone, '01234123123')


class PropertyTestCase(TestCase):
    def setUp(self):
        kate = Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')
        Property.objects.create(client = kate, address='123 langthorne road', price=29, bedrooms=2, internet=False)
        Booking.objects.create(property = Property.objects.get(address='123 langthorne road'), check_in = '2017-10-12', check_out = '2017-10-14', guest_name = 'sally', guest_email = 'sally@sally.com')

    def test_property_has_relevant_details(self):
        """Properties are stored with relevant information"""
        langthorne_road = Property.objects.get(address='123 langthorne road')
        self.assertEqual(langthorne_road.client.name, 'kate gleeson')
        self.assertEqual(langthorne_road.price, 29)
        self.assertEqual(langthorne_road.bedrooms, 2)
        self.assertEqual(langthorne_road.internet, False)

    def test_unavailable_dates(self):
        """Method returns list of unavailable dates"""
        langthorne_road = Property.objects.get(address='123 langthorne road')
        self.assertEqual(langthorne_road.unavailable_dates(), ['10-12-2017', '10-13-2017'])


class BookingTestCase(TestCase):
    def setUp(self):
        kate = Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')
        langthorne_road = Property.objects.create(client = kate, address='123 langthorne road', price=29, bedrooms=2, internet=False)
        Booking.objects.create(property = langthorne_road, check_in = '2017-10-12', check_out = '2017-10-14', guest_name = 'sally', guest_email = 'sally@sally.com')

    def test_booking_has_relevant_details(self):
        """Properties are stored with relevant information"""
        sally_booking = Booking.objects.get(pk=1)
        self.assertEqual(sally_booking.property.address, '123 langthorne road')
        self.assertEqual(sally_booking.check_in, datetime.date(2017, 10, 12))
        self.assertEqual(sally_booking.check_out, datetime.date(2017, 10, 14))
        self.assertEqual(sally_booking.guest_name, 'sally')
        self.assertEqual(sally_booking.guest_email, 'sally@sally.com')

    def test_total_price(self):
        """total_price method returns correct price"""
        sally_booking = Booking.objects.get(pk=1)
        self.assertEqual(sally_booking.total_price(), 58)
