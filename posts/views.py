from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

from .models import Post
from .forms import PostForm


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
                return redirect('mypons')
            except IntegrityError:
                return render(request, 'auth/signup.html', {'form': UserCreationForm(), 'error': 'That username has already been taken'})    
        else:
            return render(request, 'auth/signup.html', {'form': UserCreationForm(), 'error': 'Password did not match'})
        

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'auth/login.html', {'form': AuthenticationForm(), 'error': 'user is none'})
        else:
            login(request, user)
            return redirect('mypons')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def mypons(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'posts/mypons.html', {'posts': posts})


def createpons(request):
    if request.method == 'GET':
        return render(request, 'posts/createpons.html', {'form': PostForm()})
    else:
        try:
            form = PostForm(request.POST)
            newpost = form.save(commit=False)
            newpost.user = request.user
            newpost.save()
            return redirect('mypons')
        except ValueError:
            return render(request, 'posts/createpons.html', {'form': PostForm(), 'error': 'Bad data passed in. Try again'})
        

def editpons(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk, user=request.user)
    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'posts/editpons.html', {'post': post, 'form': form})
    else:
        try:
            form = PostForm(request.POST, instance=post)
            form.save()
            return redirect('mypons')
        except ValueError:
            return render(request, 'posts/editpons.html', {'posts': post, 'form': form, 'error': 'Bad info'})
        

def deletedpons(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('mypons')
