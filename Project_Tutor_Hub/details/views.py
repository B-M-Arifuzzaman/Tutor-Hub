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
from django.db.models import Q


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


@login_required
def home(request):
    '''
    This will redirect the url to the home page
    :type request: HttpResponse
    :param request: Takes the request to show home.html
    '''
    ads = Ad_Student.objects.order_by('-ad_created')
    context = {}
    context["ads"] = ads
    if "area" in request.GET:
        a = request.GET["area"]
        s = request.GET["salary"]
        sub = request.GET["subject"]
        g = request.GET["gender"]
        # result = Ad_Student.objects.filter(area__icontains=a)
        result = Ad_Student.objects.filter(
            Q(area__icontains=a) & Q(salary__gte=s)
            & Q(subject__icontains=sub) & Q(gender=g))
        context["ads"] = result
        context["search"] = "search"

    return render(request, 'home.html', context)
