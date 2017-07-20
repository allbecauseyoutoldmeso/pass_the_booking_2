from django.test import TestCase
from .models import Client
import datetime

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class ClientTestCase(TestCase):
    def setUp(self):
        Client.objects.create(name='kate gleeson', dob='1981-09-13', email='kate@kate.com', telephone='01234123123')

    def test_client_has_relevant_details(self):
        """Clients are stored with relevant information"""
        kate = Client.objects.get(name='kate gleeson')
        self.assertEqual(kate.dob, datetime.date(1981, 9, 13))
        self.assertEqual(kate.email, 'kate@kate.com')
        self.assertEqual(kate.telephone, '01234123123')


class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_homepage(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.selenium.find_elements_by_link_text('kate gleeson')
