from django.test import TestCase
from ..models import Client, Property, Booking
import datetime
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')

    def test_client_has_relevant_details(self):
        """Clients are stored with relevant information"""
        kate = Client.objects.get(name='kate gleeson')
        self.assertEqual(kate.dob, datetime.date(1981, 9, 13))
        self.assertEqual(kate.email, 'kate@kate.com')
        self.assertEqual(kate.telephone, '01234123123')

    def test_string_method(self):
        """Method returns useful label for object"""
        kate = Client.objects.get(name='kate gleeson')
        self.assertEqual(kate.__str__(), 'kate gleeson')

class PropertyTestCase(TestCase):
    def setUp(self):
        kate = Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')
        langthorne_road = Property.objects.create(client = kate, address='123 langthorne road', price=29, bedrooms=2, internet=False)
        Booking.objects.create(property = langthorne_road, check_in = '2017-10-12', check_out = '2017-10-14', guest_name = 'sally', guest_email = 'sally@sally.com')

    def test_unavailable_dates(self):
        """Method returns list of unavailable dates"""
        langthorne_road = Property.objects.get(address='123 langthorne road')
        self.assertEqual(langthorne_road.unavailable_dates(), ['20171012', '20171013'])

    def test_string_method(self):
        """Method returns useful label for object"""
        langthorne_road = Property.objects.get(address='123 langthorne road')
        self.assertEqual(langthorne_road.__str__(), '123 langthorne road')

class BookingTestCase(TestCase):
    def setUp(self):
        kate = Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')
        langthorne_road = Property.objects.create(client = kate, address='123 langthorne road', price=29, bedrooms=2, internet=False)
        Booking.objects.create(property = langthorne_road, check_in = '2017-10-12', check_out = '2017-10-14', guest_name = 'sally', guest_email = 'sally@sally.com')

    def test_total_price(self):
        """total_price method returns correct price"""
        sally_booking = Booking.objects.get(pk=1)
        self.assertEqual(sally_booking.total_price(), 58)

    def test_all_dates(self):
        """method returns array of all nights guest is staying"""
        sally_booking = Booking.objects.get(pk=1)
        self.assertEqual(sally_booking.all_dates(), ['20171012', '20171013'])

    def test_string_method(self):
        """Method returns useful label for object"""
        sally_booking = Booking.objects.get(pk=1)
        self.assertEqual(sally_booking.__str__(), "sally's booking for 123 langthorne road")
