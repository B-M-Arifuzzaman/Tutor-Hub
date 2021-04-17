'''
This program is used to take the data from the model to the templates. 
It controls the data, and returns to the template to show necessary output.
'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Ad_Student
from .forms import Ad_Student_Form

def createPostView(request):
    '''
    This will redirect the url to the create page, where a user can post an add to find tutor
    :type request: HttpResponse
    :param request: Takes the request to show post_ad.html
    '''
    User = get_user_model()
    users = User.objects.all()
    if request.method == 'GET':
        return render(request, 'ad/post_ad.html', {'form': Ad_Student_Form() })
    else:
        try: 
            form = Ad_Student_Form(request.POST)
            # newAd= form.save(commit=False)
            # newAd.user = request.user
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'ad/post_ad.html', {'form': Ad_Student_Form(), 'error': 'Limit is Crossed' })


def home(request):
    '''
    This will redirect the url to the home page, where the user can see all the posts that have published so far
    :type request: HttpResponse
    :param request: Takes the request to show home.html
    
    '''
    ads = Ad_Student.objects.order_by('-ad_created')
    return render(request, 'ad/home.html', {'ads': ads})