from django.shortcuts import render

from blog.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by("-created_on")
    return render(request, "home.html", {"posts": posts})
