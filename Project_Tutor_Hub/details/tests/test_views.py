from django.test import TestCase, Client
from django.urls import reverse
from ad.views import *


class TestViews(TestCase):
    def test_view_more_get(self):
        response = self.client.get('/view_more/')
        self.assertEquals(response.status_code, 200)

    def test_home_get(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)
