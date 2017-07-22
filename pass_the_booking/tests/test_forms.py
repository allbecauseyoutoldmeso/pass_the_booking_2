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
        print(form.errors)
        self.assertEqual(form.errors, {
            'address': ['This field is required.'],
            'price': ['This field is required.'],
            'bedrooms': ['This field is required.'],
        })
