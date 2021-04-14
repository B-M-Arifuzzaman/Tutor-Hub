from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from courses import views

urlpatterns = [
    path('createClass/',views.create_class, name='create_class'),
    path('joinClass/',views.join_class, name='join_class'),
    path('studentDashboard/',views.student_dashboard, name='student_dashboard'),
    path('tutorDashboard/',views.tutor_dashboard, name='tutor_dashboard'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
