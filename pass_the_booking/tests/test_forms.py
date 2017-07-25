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

class BookingFormTest(TestCase):

    def test_error_if_check_in_before_check_out(self):
        form = BookingForm({
            'guest_name': 'sally gleeson',
            'guest_email': 'sally@sally.com',
            'check_in': '2017-10-03',
            'check_out': '2017-10-01'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'check_out': ['Check out cannot be earlier than check in.'],
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
            'check_in': ['Check in cannot be earlier than today.'],
        })
