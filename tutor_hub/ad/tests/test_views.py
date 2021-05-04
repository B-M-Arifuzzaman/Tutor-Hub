'''
This program will use unittest to test ad app's views.py
'''

from django.test import TestCase, Client
from django.urls import reverse
from ad.views import *

class TestViews(TestCase):
    def test_find_tutor_get(self):
        response = self.client.get('/find_tutor/')
        self.assertEquals(response.status_code, 200)
    
    def test_find_student_get(self):
        response = self.client.get('/find_student/')
        self.assertEquals(response.status_code, 200)
        
    def test_home_get(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)
        