from django.shortcuts import render
from django.shortcuts import  redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from courses.forms  import  CreateClassForm
from courses.models import Class,Lecture
from home.models import Tutor,Student
from django.views.generic import TemplateView,DetailView,ListView,FormView,CreateView,UpdateView,DeleteView

def create_class(request):
    form = CreateClassForm()
    if request.method == 'POST':
        form = CreateClassForm(request.POST)
        if form.is_valid():
            new_class = form.save()
            new_class.tutor = request.user.tutor
            new_class.save()
            return redirect('teacher_dashboard')
    context = {'form': form}
    return render(request, 'courses/create_class.html', context)


def join_class(request):
    if request.method == 'POST':
        class_code = request.POST.get('class_code')
        try:
            myClass = Class.objects.get(class_code=class_code)
            student = request.user.student
            myClass.students.add(student)
            return redirect('student_dashboard')
        except Class.DoesNotExist:
            messages.info(request, "Invalid Class Code")
    context = {}
    return render(request, 'courses/join_class.html', context)


def student_dashboard(request):
    student = request.user.student
    classes = Class.objects.filter(students=student)
    context = {'classes': classes}
    return render(request, 'courses/student_dashboard.html', context)

def tutor_dashboard(request):
    tutor = request.user.tutor
    classes = Class.objects.filter(tutor=tutor)
    context = {'classes': classes}
    return render(request, 'courses/tutor_dashboard.html', context)


def LectureListView(request, class_code):
    # student = request.user.student
    class_object = Class.objects.get(class_code=class_code)
    lectures = class_object.lessons.all()
    context = {'lectures': lectures, 'class': class_object}
    return render(request, 'courses/lecture_list_view.html', context)