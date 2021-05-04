'''
This program will use unittest to test ad app's models.py
'''
from django.test import TestCase
from ad.models import AdStudent, AdTutor
from django.contrib.auth.models import User

class TestModels(TestCase):
    '''
    This is a conceptual Unittest child case class for testing models.py. 
    :param TestCase: It inherits built-in child functionalities of django `unittest`, which handels all test cases.
    :type SimpleTestCase: functions
    '''
    def test_model_string_student(self):
        '''
        This will test the __str__ function to store student ad title.
        :param self: Takes the self content and pass. 
        :type self: string
        :return: returns a request to check the title value. 
        :rtype: assertEqual , bool
        '''
        user = User.objects.create_user(username="name", email="email@mail.com", password="Pass12345")
        title = AdStudent(user=user, title='Django Testing')
        title.save()
        self.assertEqual(str(title), 'Django Testing')
        
    def test_model_string_tutor(self):
        '''
        This will test the __str__ function to store tutor ad title.
        :param self: Takes the self content and pass. 
        :type self: string
        :return: returns a request to check the title value. 
        :rtype: assertEqual , bool
        '''
        user = User.objects.create_user(username="name2", email="email@mail.com", password="Pass12345")
        title = AdTutor(user=user, title='Django Testing')
        title.save()
        self.assertEqual(str(title), 'Django Testing')
        