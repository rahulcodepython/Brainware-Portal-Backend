from django.shortcuts import render, redirect
from authentication.models import User
from django.contrib.auth import login, authenticate


def login(request):
    return render(request, 'login.html')


def loginUser(request):
    user = authenticate(request, username="rahul", password="admin")
    print("hi")

    if user:
        login(request, user)
        return redirect('dashboard_template')

def dashboard(request):
    # if not request.user.is_authenticated:
    #     return redirect('login_template')
    return render(request, 'dashboard.html')

def profile(request):
    return render(request, 'profile.html')