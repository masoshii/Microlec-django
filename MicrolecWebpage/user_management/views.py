from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponseForbidden
from django.db import IntegrityError
from .models import User

def is_staff_user(user):
    return user.is_staff


def logout_view(request):
    logout(request)
    return redirect('index')



@login_required
@user_passes_test(is_staff_user, login_url='login')
def userlist(request):
    users = User.objects.all()
    user_data = [
        {
            'id': user.id,
            'email': user.email,
            'names': user.names,
            'lnames': user.lnames,
            'run': user.run,
            'salt': user.salt,
            'password_hash': user.password_hash,
            'is_active': user.is_active,
            'is_staff': user.is_staff,
        }
        for user in users
    ]
    return JsonResponse(user_data, safe=False)


