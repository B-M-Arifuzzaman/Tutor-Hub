from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from django.forms import ModelForm
from home.models import Student,Tutor
from courses.models import Class,Lecture


class CreateClassForm(ModelForm):
    title = forms.CharField(label='Course Name', max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    class Meta:
        model = Class
        fields = ['title', 'description']

class CreateLectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ('name','position','video','ppt','notes')


