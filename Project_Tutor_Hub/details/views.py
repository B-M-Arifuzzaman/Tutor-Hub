'''
This program is used to take the data from the model to the templates. 
It controls the data, and returns to the template to show necessary output.
'''
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Profile
from django.contrib.auth.models import User
from .models import Ad_Student
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def view_more(request, pk):
    '''
    This will redirect the url to the view more page
    :type request: HttpResponse
    :param request: Takes the request to show view_more.html
    :param pk: Gets value of id of the selected ad
    '''
    ad = Ad_Student.objects.get(id=pk)
    return render(request, 'view_more.html', {'ad': ad})


