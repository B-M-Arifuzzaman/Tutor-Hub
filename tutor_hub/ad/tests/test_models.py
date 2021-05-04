'''
This program will use unittest to test ad app's models.py
'''
from django.test import TestCase
from ad.models import AdStudent, AdTutor
from django.contrib.auth.models import User

class TestModels(TestCase):
    
    def test_model_string_student(self):
        user = User.objects.create_user(username="name", email="email@mail.com", password="Pass12345")
        title = AdStudent(user=user, title='Django Testing')
        title.save()
        self.assertEqual(str(title), 'Django Testing')
        
    def test_model_string_tutor(self):
        user = User.objects.create_user(username="name2", email="email@mail.com", password="Pass12345")
        title = AdTutor(user=user, title='Django Testing')
        title.save()
        self.assertEqual(str(title), 'Django Testing')
        