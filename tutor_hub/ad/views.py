from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Ad_Student
from .forms import Ad_Student_Form

def createPostView(request):
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
    ads = Ad_Student.objects.order_by('-ad_created')
    return render(request, 'ad/home.html', {'ads': ads})