from django.shortcuts import render
from django.http import HttpResponse
# from .models import Profile
from django.contrib.auth.models import User
from .models import Ad_Student
from django.contrib.auth.decorators import login_required


from django.urls import reverse


def view_more(request):
    '''
    This will redirect the url to the view more page
    :type request: HttpResponse
    :param request: Takes the request to show view_more.html

    '''
    ad = Ad_Student.objects.get(id=1)
    return render(request, 'view_more.html', {'ad': ad})
