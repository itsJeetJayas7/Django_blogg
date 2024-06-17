from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': "Colonell",
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2024'
    },
{
        'author': "John Purdue",
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2024'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context )

def test1(request):
    return render(request, "blog/test1.html")

def about(request):
    return render(request, "blog/about.html")
