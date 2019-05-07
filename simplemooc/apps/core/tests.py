from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class HomeViewTestg(TestCase):

    def test_home_status_code(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)