from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("test1/", views.test1, name="blog-test"),
    path("about/", views.about, name="blog-about"),
]