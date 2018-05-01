from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User

from . import models

# Create your views here.
def auth(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'GET':
        return HttpResponse(render(request, 'login.html'))
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Error. User hasn\'t logged')

@login_required
def exit(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    print(1)

    if request.method == 'GET':
        return HttpResponse(render(request, 'register.html'))
    else:
        username = request.POST['username']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']

        if password != password_repeat:
            return HttpResponse('Error. First password not equal second password.')

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            
            login(request, user)
        except:
            return HttpResponse('Error.')

        return redirect('index')
