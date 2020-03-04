from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required
def login(request):
    return render(request, 'dashboard/login.html', {'title': 'Log in'})


@login_required
def logout(request):
    return render(request, 'dashboard/logout.html', {'title': 'Log out'})


@login_required
def landing(request):
    return render(request, 'dashboard/index.html')


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'dashboard/home.html', context)
