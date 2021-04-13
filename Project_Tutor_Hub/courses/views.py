from django.shortcuts import render
from django.shortcuts import  redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from courses.forms  import  CreateClassForm
from courses.models import Student,Tutor


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
