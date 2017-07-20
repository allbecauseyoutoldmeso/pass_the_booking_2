from django.test import TestCase
from .models import Client
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
