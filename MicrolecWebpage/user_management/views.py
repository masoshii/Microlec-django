from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import User

def usermgr(request):
    return render(request, 'usermgr.html')

def logout(request):
    logout(request)
    return redirect(request, '')

