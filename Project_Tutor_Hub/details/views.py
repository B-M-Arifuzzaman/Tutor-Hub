'''
This program is the controller that fetch data from models.py and send it to the template file. 
'''
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Profile
from django.contrib.auth.models import User
from .models import Ad_Student, Ad_Tutor
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@login_required
def view_more(request, pk):
    '''
    This will redirect the url to the view_more page, where a logged in user can see details of a post on which he clicks the link View More.
    :param request: Takes the request to show view_more.html
    :type request: HttpResponse
    :param pk: Gets value of the selected ad's id through a link
    :type pk: int
    :return: returns a request for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    '''
    stu_ad = Ad_Student.objects.get(id=pk)
    tut_ad = Ad_Tutor.objects.get(id=pk)
    return render(request, 'view_more.html', {'stu_ad': stu_ad, 'tut_ad': tut_ad})


# @login_required
# def home(request):
#     '''
#     This will redirect the url to the home page
#     :type request: HttpResponse
#     :param request: Takes the request to show home.html
#     '''
#     ads_s = Ad_Student.objects.order_by('-ad_created')
#     ads_t = Ad_Tutor.objects.order_by('-ad_created')
#     context = {}
#     context["ads_s"] = ads_s
#     context["ads_t"] = ads_t
#     if "area" in request.GET:
#         a = request.GET["area"]
#         s = request.GET["salary"]
#         sub = request.GET["subject"]
#         g = request.GET["gender"]
#         # result = Ad_Student.objects.filter(area__icontains=a)
#         result_s = Ad_Student.objects.filter(
#             Q(area__icontains=a) & Q(salary__gte=s)
#             & Q(subject__icontains=sub) & Q(gender=g))
#         result_t = Ad_Tutor.objects.filter(
#             Q(expected_area__icontains=a) & Q(expected_salary__gte=s)
#             & Q(subject__icontains=sub) & Q(gender=g))
#         context["ads_s"] = result_s
#         context["ads_t"] = result_t
#         context["search"] = "search"
#
#   return render(request, 'home.html', context)


@login_required
def home(request):
    '''
    This will redirect the url to the home page, where a logged in user can see posts of other user.
    :param request: Takes the request to show home.html
    :type request: HttpResponse
    :return: returns a request for a html page with form data as dictonary format
    :rtype: render request,html page,dictonary
    '''
    studentAd_list = Ad_Student.objects.order_by('-ad_created')
    tutorAd_list = Ad_Tutor.objects.order_by('-ad_created')
    context = {}
    if "area" in request.GET:
        a = request.GET["area"]
        s = request.GET["salary"]
        sub = request.GET["subject"]
        g = request.GET["gender"]
        # result = Ad_Student.objects.filter(area__icontains=a)
        result_s = Ad_Student.objects.filter(
            Q(area__icontains=a) & Q(salary__gte=s)
            & Q(subject__icontains=sub) & Q(gender=g))
        result_t = Ad_Tutor.objects.filter(
            Q(expected_area__icontains=a) & Q(expected_salary__gte=s)
            & Q(subject__icontains=sub) & Q(gender=g))
        studentAd_list = result_s
        tutorAd_list = result_t
        context["search"] = "search"

    # Paginator for Student Posts
    paginator = Paginator(studentAd_list, 5)
    page = request.GET.get('page')
    try:
        studentAds = paginator.page(page)
    except PageNotAnInteger:
        studentAds = paginator.page(1)
    except EmptyPage:
        studentAds = paginator.page(paginator.num_pages)

    # Paginator for Tutor Posts
    paginator = Paginator(tutorAd_list, 5)
    page = request.GET.get('page')
    try:
        tutorAds = paginator.page(page)
    except PageNotAnInteger:
        tutorAds = paginator.page(1)
    except EmptyPage:
        tutorAds = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'studentAds': studentAds, 'tutorAds': tutorAds}, context)
