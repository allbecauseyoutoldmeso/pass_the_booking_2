from django.test import TestCase
from ..models import Client, Property, Booking
from ..forms import ClientForm, PropertyForm, BookingForm
import datetime

class ClientFormTest(TestCase):

    def test_valid_data(self):
        form = ClientForm({
            'name': 'kate gleeson',
            'email': 'kate@kate.com',
            'dob': '1981-09-13',
            'telephone': '12345123123'
        })
        self.assertTrue(form.is_valid())
        client = form.save()
        self.assertEqual(client.name, 'kate gleeson')
        self.assertEqual(client.email, 'kate@kate.com')
        self.assertEqual(client.dob, datetime.date(1981, 9, 13))
        self.assertEqual(client.telephone, '12345123123')

    def test_blank_data(self):
        form = ClientForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['This field is required.'],
            'dob': ['This field is required.'],
            'email': ['This field is required.'],
            'telephone': ['This field is required.'],
        })

class PropertyFormTest(TestCase):

    def test_valid_data(self):
        form = PropertyForm({
            'address': '123 langthorne road',
            'price': 29,
            'bedrooms': 2,
            'internet': True
        })
        self.assertTrue(form.is_valid())
        property = form.save(commit=False)
        property.client = Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')
        property.save()
        self.assertEqual(property.address, '123 langthorne road')
        self.assertEqual(property.price, 29)
        self.assertEqual(property.bedrooms, 2)
        self.assertEqual(property.internet, True)

    def test_blank_data(self):
        form = PropertyForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'address': ['This field is required.'],
            'price': ['This field is required.'],
            'bedrooms': ['This field is required.'],
        })

class BookingFormTest(TestCase):

    def test_valid_data(self):
        form = BookingForm({
            'guest_name': 'sally gleeson',
            'guest_email': 'sally@sally.com',
            'check_in': '2017-10-01',
            'check_out': '2017-10-03'
        })
        self.assertTrue(form.is_valid())
        booking = form.save(commit=False)
        kate = Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')
        langthorne_road = Property.objects.create(client = kate, address='123 langthorne road', price=29, bedrooms=2, internet=False)
        booking.property = langthorne_road
        booking.save()
        self.assertEqual(booking.guest_name, 'sally gleeson')
        self.assertEqual(booking.guest_email, 'sally@sally.com')
        self.assertEqual(booking.check_in, datetime.date(2017, 10, 1))
        self.assertEqual(booking.check_out, datetime.date(2017, 10, 3))

    def test_blank_data(self):
        form = BookingForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'guest_name': ['This field is required.'],
            'guest_email': ['This field is required.'],
            'check_in': ['This field is required.'],
            'check_out': ['This field is required.'],
        })

    def test_error_if_check_in_before_check_out(self):
        form = BookingForm({
            'guest_name': 'sally gleeson',
            'guest_email': 'sally@sally.com',
            'check_in': '2017-10-03',
            'check_out': '2017-10-01'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'check_out': ['check out cannot be earlier than check in.'],
        })

    def test_error_if_check_in_before_today(self):
        form = BookingForm({
            'guest_name': 'sally gleeson',
            'guest_email': 'sally@sally.com',
            'check_in': '2017-07-21',
            'check_out': '2017-07-25'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'check_in': ['check in cannot be earlier than today.'],
        })
