from django.db import models
from django.contrib.auth.models import User
import os
from django.urls import reverse


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')

#     def __str__(self):
#         return f'{self.user.username} Profile'


class Ad_Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    area = models.CharField(max_length=150, null=True, blank=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    class_level = models.CharField(max_length=150, null=True, blank=True)
    days = models.DecimalField(decimal_places=0, max_digits=7)
    salary = models.DecimalField(decimal_places=3, max_digits=10)
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
        return self.title

    def get_absolute_url(self):
        return reverse('ad/home.html')
