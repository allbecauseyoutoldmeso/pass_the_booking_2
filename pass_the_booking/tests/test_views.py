from django.test import TestCase

class ProjectTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'welcome to pass the booking')

    def test_client_list(self):
        Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')
        response = self.client.get('/clients/')
        self.assertContains(response, 'kate gleeson')
