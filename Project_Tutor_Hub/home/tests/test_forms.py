from django.contrib.auth.models import User
from django.test import TestCase
from home.forms import EditForm_Tutor, EditForm_Student

class TestForms(TestCase):
    def test__EditForm_Tutor_valid_data(self):
        tu1 = User.objects.create_user(username="David", email="david_malan@gmail.com", password="12254")
        form = EditForm_Tutor(data={
            'user': tu1, 
            'institutiom':'Harvard',
            'area': 'USA', 
            'subject': 'CSE', 
            'class_level': 'Bsc',
            'salary': '60000',
            'gender': 'Male',
        })
        self.assertTrue(form.is_valid())
    
    def test__EditForm_Student_valid_data(self):
        st1 = User.objects.create_user(username="Bill", email="bill_010@gmail.com", password="1225441@")
        form = EditForm_Student(data={
            'user': st1, 
            'institutiom':'SPSC',
            'area': 'Bashundhara', 
            'subject': 'math', 
            'class_level': '5',
            'gender': 'Male',
        })
        self.assertTrue(form.is_valid())