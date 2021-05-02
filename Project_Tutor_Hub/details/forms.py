'''
This program will create a django model form.
'''
from django import forms
from django.forms import ModelForm, fields
from .models import Ad_Student


class Ad_Student_Form(ModelForm):
    '''
    This is a conceptual Form representation of Class table for student ads.
    :param ModelForm: It creates built-in html form of django, which handels all validations in django Admin panel.
    :type ModelForm: model, fields
    '''
    class Meta:
        model = Ad_Student
        fields = '__all__'


class Ad_Tutor_Form(ModelForm):
    '''
    This is a conceptual Form representation of Class table for tutor ads.
    :param ModelForm: It creates built-in html form of django, which handels all validations in django Admin panel.
    :type ModelForm: model, fields
    '''
    class Meta:
        model = Ad_Tutor
        fields = '__all__'
