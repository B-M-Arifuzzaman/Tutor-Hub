from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from courses import views

urlpatterns = [
    path('createClass/',views.create_class, name='create_class'),
    path('joinClass/',views.join_class, name='join_class'),
    path('studentDashboard/',views.student_dashboard, name='student_dashboard'),
    path('tutorDashboard/',views.tutor_dashboard, name='tutor_dashboard'),
    path('student/class/<slug:slug>/',views.student_lecture_list_View, name='student_lecture_list_view'),
    path('tutor/class/<slug:slug>/',views.tutor_lecture_list_View, name='tutor_lecture_list_view'),
    path('tutor/class/<slug:slug>/newLecture',views.create_lecture_view, name='create_lecture'),
    #path('tutor/createLecture',views.create_lecture_view, name='create_lecture'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
