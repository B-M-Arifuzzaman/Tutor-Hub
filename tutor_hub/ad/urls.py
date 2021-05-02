from django.urls import path
from . import views

urlpatterns = [
    path('find-Tutor/', views.student_Ad, name='findTutor'),
    path('find-Student/', views.tutor_Ad, name='findStudent'),
    path('home/', views.home, name='home'),
    path('profile/user/<int:user_pk>', views.ad_profile, name='profile_user'),
    path('myAd/', views.myAd, name='myAd'),
    path('myAd/delete/student/post/<int:post_pk>', views.delete_post_Student, name='delete_post_student'),
    path('myAd/delete/tutor/post/<int:post_pk>', views.delete_post_Tutor, name='delete_post_tutor'),
]