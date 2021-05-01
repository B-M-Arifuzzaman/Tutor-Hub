from django.urls import path
from . import views

urlpatterns = [
    path('find-Tutor/', views.student_Ad, name='findTutor'),
    path('find-Student/', views.tutor_Ad, name='findStudent'),
    path('home/', views.home, name='home'),
    path('myAd/', views.myAd, name='myAd'),
    path('myAd/delete/<int:post_pk>', views.delete_post, name='delete_post'),
]