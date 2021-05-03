'''
This program is the controller that fetch data from models.py and send it to the template file. 
'''
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import AdStudent, AdTutor
from .forms import AdStudentForm, AdTutorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from home.models import Student,Tutor
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# feature - 1
@login_required
def student_ad(request):
    '''
    This will redirect the url to the student_ad page, where a logged in student can create a new post to find a tutor.
    :param request: Takes the request to show student_ad.html
    :type request: HttpResponse
    :return: returns a request for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    '''
    User = get_user_model()
    users = User.objects.all()
    if request.method == 'GET':
        return render(request, 'ad/student_ad.html', {'form': AdStudentForm() })
    else:
        try: 
            form = AdStudentForm(request.POST)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'ad/student_ad.html', {'form': AdStudentForm(), 'error': 'Limit is Crossed' })


@login_required
def tutor_ad(request):
    '''
    This will redirect the url to the student_ad page, where a logged in tutor can create a new post to find a student.
    :param request: Takes the request to show tutor_ad.html
    :type request: HttpResponse
    :return: returns a request for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    '''
    User = get_user_model()
    users = User.objects.all()
    if request.method == 'GET':
        return render(request, 'ad/tutor_ad.html', {'form': AdTutorForm() })
    else:
        try: 
            form = AdTutorForm(request.POST)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'ad/tutor_ad.html', {'form': AdTutorForm(), 'error': 'Limit is Crossed' })

@login_required
def home(request):
    '''
    This will redirect the url to the home page, where a logged in user can see posts of other user.
    :param request: Takes the request to show home.html
    :type request: HttpResponse
    :return: returns a request for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    '''
    student_ad_list = AdStudent.objects.order_by('-ad_created')
    tutor_ad_list = AdTutor.objects.order_by('-ad_created')
    
    #Paginator for Student Posts
    paginator = Paginator(student_ad_list, 5)
    page = request.GET.get('page')
    try:
        student_ads = paginator.page(page)
    except PageNotAnInteger:
        student_ads = paginator.page(1)
    except EmptyPage:
        student_ads = paginator.page(paginator.num_pages)
    
    #Paginator for Tutor Posts
    paginator = Paginator(tutor_ad_list, 5)
    page = request.GET.get('page')
    try:
        tutor_ads = paginator.page(page)
    except PageNotAnInteger:
        tutor_ads = paginator.page(1)
    except EmptyPage:
        tutor_ads = paginator.page(paginator.num_pages)
        
    return render(request, 'ad/home.html', {'student_ads': student_ads, 'tutor_ads': tutor_ads})

# feature - 2
@login_required
def my_ad(request):
    '''
    This will redirect the url to the myad page, where a user can see his own posts.
    :param request: Takes the request to show myad.html
    :type request: HttpResponse
    :return: returns a request for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    '''
    myStudentAds = Ad_Student.objects.filter(user=request.user).order_by('-ad_created')
    myTutorAds = Ad_Tutor.objects.filter(user=request.user).order_by('-ad_created')
    return render(request, 'ad/myad.html', {'myStudentAds': myStudentAds, 'myTutorAds': myTutorAds})


@login_required
def delete_post_student(request,post_pk):
    '''
    This will redirect the url to the delete_post_student page, where a student can delete his own posts.
    :param request: Takes the request to show delete_post_student.html
    :type request: HttpResponse
    :param post_pk: Takes the id of the post to delete exact post
    :type post_pk: integer
    :return: returns a request for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    '''
    student_post = Ad_Student.objects.get(id=post_pk)
    if request.method == 'POST':
        student_post.delete()
        return redirect('myAd')
    return render(request, 'ad/delete_post_student.html', {'student_post': student_post})

@login_required
def delete_post_tutor(request,post_pk):
    '''
    This will redirect the url to the delete_post_tutor page, where a tutor can delete his own posts.
    :param request: Takes the request to show delete_post_tutor.html
    :type request: HttpResponse
    :param post_pk: Takes the id of the post to delete exact post
    :type post_pk: integer
    :return: returns a request for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    '''
    tutor_post = Ad_Tutor.objects.get(id=post_pk)
    if request.method == 'POST':
        tutor_post.delete()
        return redirect('myAd')
    return render(request, 'ad/delete_post_tutor.html', {'tutor_post': tutor_post})

@login_required
def ad_profile(request, user_pk):
    '''
    This will redirect the url to the ad_profile page, where a user can see other user's profile through ad.
    :param request: Takes the request to show delete_post_tutor.html
    :type request: HttpResponse
    :param post_pk: Takes the id of the user to redirect exact user's profile.
    :type post_pk: integer
    :return: returns a request for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    '''
    User = get_user_model()
    user = User.objects.get(id=user_pk)
    return render(request, 'ad/ad_profile.html', {'user': user})
    
    
    