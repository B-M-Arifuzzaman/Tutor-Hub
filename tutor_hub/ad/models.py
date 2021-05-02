'''
This program will create database file for Advertise feature.
'''
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse     

class AdStudent(models.Model):
    '''
    This is a conceptual Database representation of Class table for student ads.
    :param models.Model: It inherits built-in functionalities of django `models.Model`, which handels all validations in django Admin panel.
    :type ModelForm: model.Model
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    area = models.CharField(max_length=150, null=True, blank=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    class_level = models.CharField(max_length=150, null=True, blank=True)
    days = models.DecimalField(decimal_places=0, max_digits=2)
    salary = models.DecimalField(decimal_places=0, max_digits=10)
    male ='male'
    female = 'female'
    other = 'other'
    genders = [
        (male,'male'),
        (female,'female'),
        (other,'other'),
    ]
    gender = models.CharField(max_length=15, choices=genders,default=male,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    request_confirmation = models.BooleanField(default=False)
    ad_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        '''
        This will show the title of students's ad in the admin panel.
        :param self: Takes the self's variable name. 
        :type self: string
        :return: returns a reference to the instance object on which it was called.
        :rtype: model variable name
        '''
        return self.title
    
    def get_absolute_url(self):
        '''
        This will reverse a url to home page.
        :param self: Takes the self's reverse url. 
        :type self: HttpResponse
        :return: returns a request for a reverse html page with form data as dictonary format
        :rtype: reverse html
        '''
        return reverse('ad/home.html')

class AdTutor(models.Model):
    '''
    This is a conceptual Database representation of Class table for tutor ads.
    :param models.Model: It inherits built-in functionalities of django `models.Model`, which handels all validations in django Admin panel.
    :type ModelForm: model.Model
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    expected_area = models.CharField(max_length=150, null=True, blank=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    class_level = models.CharField(max_length=150, null=True, blank=True)
    days = models.DecimalField(decimal_places=0, max_digits=7)
    expected_salary = models.DecimalField(decimal_places=0, max_digits=10)
    male ='male'
    female = 'female'
    other = 'other'
    genders = [
        (male,'male'),
        (female,'female'),
        (other,'other'),
    ]
    gender = models.CharField(max_length=15, choices=genders,default=male,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    request_confirmation = models.BooleanField(default=False)
    ad_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        '''
        This will show the title of tutor's ad in the admin panel.
        :param self: Takes the self's variable name. 
        :type self: string
        :return: returns a reference to the instance object on which it was called.
        :rtype: self .model variable name
        '''
        return self.title
    
    
    
