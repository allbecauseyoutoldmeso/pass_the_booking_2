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
        print(form.errors)
        self.assertEqual(form.errors, {
            'name': ['This field is required.'],
            'dob': ['This field is required.'],
            'email': ['This field is required.'],
            'telephone': ['This field is required.'],
        })
