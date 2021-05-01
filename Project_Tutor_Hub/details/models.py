'''
This program is used to create a database table.
Each of the variables will be a column of a table. 
'''
from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse


def path_and_rename(instance, filename):
    upload_to = 'images/'
    extension = filename.split('.')[-1]

    # get filename
    if instance.user.username:
        filename = 'User_profile_pictures/{}.{}'.format(
            instance.user.username, extension)

    return os.path.join(upload_to, filename)


class Ad_Student(models.Model):
    '''
    This class will create a table Ad_Student, where a student will fill the form to request for a tutor.
    In that table the fields will be the variables, fields attributes are also defined here. 
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usr_type = models.CharField(default='st', max_length=10)
    title = models.CharField(max_length=150, null=True, blank=True)
    area = models.CharField(max_length=150, null=True, blank=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    class_level = models.CharField(max_length=150, null=True, blank=True)
    days = models.DecimalField(decimal_places=0, max_digits=7)
    salary = models.DecimalField(decimal_places=3, null=True, max_digits=10)
    male = 'male'
    female = 'female'
    other = 'other'
    genders = [
        (male, 'male'),
        (female, 'female'),
        (other, 'other'),
    ]
    gender = models.CharField(
        max_length=15, choices=genders, default=male, null=True, blank=True)
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
        return reverse('home.html')


class Ad_Tutor(models.Model):
    '''
    This class will create a table Ad_Tutor, where a tutor will fill the form to request for a student.
    In that table the fields will be the variables, fields attributes are also defined here. 
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usr_type = models.CharField(default='tt', max_length=10)
    title = models.CharField(max_length=150, null=True, blank=True)
    expected_area = models.CharField(max_length=150, null=True, blank=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    class_level = models.CharField(max_length=150, null=True, blank=True)
    days = models.DecimalField(decimal_places=0, max_digits=7)
    expected_salary = models.DecimalField(
        decimal_places=0, null=True, max_digits=10)
    male = 'male'
    female = 'female'
    other = 'other'
    genders = [
        (male, 'male'),
        (female, 'female'),
        (other, 'other'),
    ]
    gender = models.CharField(
        max_length=15, choices=genders, default=male, null=True, blank=True)
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


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    institution = models.CharField(max_length=150, null=True, blank=True)
    department = models.CharField(max_length=150, null=True, blank=True)
    class_level = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    area = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)

    male = 'male'
    female = 'female'
    other = 'other'
    genders = [
        (male, 'male'),
        (female, 'female'),
        (other, 'other'),
    ]
    gender = models.CharField(
        max_length=15, choices=genders, default=male, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    bio = models.CharField(max_length=450, blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to=path_and_rename, verbose_name='profile picture', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    institution = models.CharField(max_length=150, null=True, blank=True)
    subject_teach = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    area = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    salary_per_month = models.CharField(max_length=150, null=True, blank=True)
    preffered_area = models.CharField(max_length=150, null=True, blank=True)
    online_teach_exp = models.FloatField(max_length=100, null=True, blank=True)
    total_teach_exp = models.FloatField(max_length=100, null=True, blank=True)
    qualification = models.CharField(max_length=250, null=True, blank=True)

    inhouse = 'Inhouse'
    online = 'Online'
    both = 'Inhouse & Online'
    tutor_types = [
        (inhouse, 'Inhouse'),
        (online, 'Online'),
        (both, 'Inhouse & Online'),
    ]
    tutor_type = models.CharField(
        max_length=25, choices=tutor_types, default=inhouse, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    bio = models.CharField(max_length=450, blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to=path_and_rename, verbose_name='profile picture', blank=True, null=True)

    def __str__(self):
        return self.user.username
