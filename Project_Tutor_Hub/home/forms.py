from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from django.forms import ModelForm
from home.models import Student,Tutor

'''
    This is a conceptual Form representation of Class table for Edit Form for the Tutor Profile
    :param ModelForm: It creates built-in html form of django, which handels all validations in django Admin panel.
    :type ModelForm: model, fields
    '''

class EditForm_Tutor(ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'
        exclude = ['user']

'''
    This is a conceptual Form representation of Class table for Edit Form for the Student Profile
    :param ModelForm: It creates built-in html form of django, which handels all validations in django Admin panel.
    :type ModelForm: model, fields
    '''
        
class EditForm_Student(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['user']

'''
    This is a conceptual Form representation of Class table for the user signup
    :param ModelForm: It creates built-in html form of django, which handels all validations in django Admin panel.
    :type ModelForm: model, fields
    '''

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    group = forms.ModelChoiceField(queryset=Group.objects.all(),required=True)
    email = forms.EmailField()
    class Meta:
        model = User

        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'group']


