from django.shortcuts import render
from django.http import HttpResponse
from  .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context )

def test1(request):
    return render(request, "blog/test1.html")

def about(request):
    return render(request, "blog/about.html")
