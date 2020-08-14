from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.
def home(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        firstname = req.POST.get('firstName')
        lastname = req.POST.get('lastName')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        gender = req.POST.get('gender')
        try:
            user = User.objects.create_user(
            username=username, 
            password=password, 
            first_name=firstname,
            last_name=lastname,
            email=email)
            userprofile = UserProfile(user=user, phone=phone, gender=gender)
            userprofile.save()
            return render(req, "part1/SearchUser.html")
        except:
            return render(req, "part1/Home.html") 
    return render(req, "part1/Home.html")


def searchUser(req):
    if req.method == 'POST':
        try:
            email = req.POST.get('email')
            user = User.objects.get(email=email)
            userprofile = UserProfile.objects.get(user=user)
            data = {
                'name': user.first_name + " " + user.last_name,
                'email': user.email,
                'phone': userprofile.phone,
                'gender': userprofile.gender
            }
            return render(req, "part1/ShowDetails.html", {'data': data, 'message': 'Found registered user' })
        except:
            return render(req, "part1/ShowDetails.html", {'message': 'No registered user found' })
    return render(req, "part1/SearchUser.html")