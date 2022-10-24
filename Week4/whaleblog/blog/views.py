from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def view_post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "post.html", {"post": post})

@login_required
def like_post(request, slug):
    post = Post.objects.get(slug=slug)
    post.likes += 1
    post.save()
    return redirect('home')
