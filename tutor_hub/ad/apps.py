'''
This program will create a visual database in Admin panel.
'''
from django.apps import AppConfig


class AdConfig(AppConfig):
    '''
    This is a Visual Database representation of all apps in Admin panel.
    :param AppConfig: It configures the database in Admin panel.
    :type AppConfig: string
    '''
    name = 'ad'
