'''
This program is used to create a database table.
Each of the variables will be a column of a table. 
'''
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse     

class Ad_Student(models.Model):
    '''
    This class will create a table Ad_Student, where a student will fill the form to request for a tutor.
    In that table the fields will be the variables, fields attributes are also defined here. 
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
        This will take the self value of this function. 
        :type self: string
        :param self: Takes the object representation in string format.
        '''
        return self.title
    
    def get_absolute_url(self):
        '''
        This will take the self value of this function. 
        :type self: HttpResponse
        :param self: Takes the request to show home.html
        '''
        return reverse('ad/home.html')

class Ad_Tutor(models.Model):
    '''
    This class will create a table Ad_Tutor, where a tutor will fill the form to request for a tutor.
    In that table the fields will be the variables, fields attributes are also defined here. 
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    expected_area = models.CharField(max_length=150, null=True, blank=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    class_level = models.CharField(max_length=150, null=True, blank=True)
    days = models.DecimalField(decimal_places=0, max_digits=7)
    expected_salary = models.DecimalField(decimal_places=1000, max_digits=50000)
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
            This will take the self value of this function. 
            :type self: string
            :param self: Takes the object representation in string format.
            '''
        return self.title
    
    
    
