from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

from .models import Post


def home(request):
    posts = Post.objects.all()[:5]
    return render(request, 'posts/home.html', {'posts': posts})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'auth/signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('allpons')
            except IntegrityError:
                return render(request, 'auth/signup.html', {'form': UserCreationForm(), 'error': 'That username has already been taken'})    
        else:
            return render(request, 'auth/signup.html', {'form': UserCreationForm(), 'error': 'Password did not match'})
        

def allpons(request):
    return render(request, 'posts/allpons.html')
