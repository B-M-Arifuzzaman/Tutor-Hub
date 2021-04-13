from django.urls import path
from courses import views

urlpatterns = [
    path('createClass/',views.create_class, name='create_class'),
    path('joinClass/',views.join_class, name='join_class'),
    
]
