from django.shortcuts import render
from authentication.models import User


def home(request):
    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'home.html', context)


def login(request):
    return render(request, 'login.html')
