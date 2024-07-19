from django.shortcuts import render

from .models import Post


def home(request):
    posts = Post.objects.all()[:5]
    return render(request, 'posts/home.html', {'posts': posts})
