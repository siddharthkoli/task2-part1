from django.urls import path
from part1 import views

urlpatterns = [
    path("", views.home, name="home"),
    path("searchUser", views.searchUser, name="searchUser"),
]