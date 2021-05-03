'''
This program will use unittest to test details app's urls.py
'''

from django.test import SimpleTestCase
from django.urls import resolve, reverse
from details.views import view_more, home


class TestUrls(SimpleTestCase):
    '''
    This is a conceptual Unittest child case for testing urls.py. 
    :param SimpleTestCase: It inherits built-in child functionalities of django `unittest`, which handels all test cases.
    :type SimpleTestCase: functions
    '''

    def test_view_more_url_resolves(self):
        '''
        This will test the view_more url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('view_more', args[1])
        self.assertEqual(resolve(url).func, view_more)

    def test_home_url_resolves(self):
        '''
        This will test the home url.
        :param self: Takes the self content and pass. 
        :type self: Boolean
        :return: returns a request to check the url pattern. 
        :rtype: assertEqual resolve, url
        '''
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)
