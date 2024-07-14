from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponseForbidden
from django.db import IntegrityError
from .models import User

def is_staff_user(user):
    return user.is_staff


def usermgr(request):
    if request.user.is_authenticated:
        return render(request, 'usermgr.html', {'user': request.user})

    if request.method == 'POST':
        if 'signup' in request.POST:
            email = request.POST['register_email']
            password = request.POST['register_password']
            names = request.POST['register_names']
            lnames = request.POST['register_lnames']
            run = request.POST['register_run']
            try:
                user = User.objects.create_user(email=email, password=password, names=names, lnames=lnames, run=run)
                login(request, user)
                return redirect('usermgr')
            except IntegrityError as e:
                error_message = str(e)
                if 'unique constraint' in error_message.lower():
                    if 'email' in error_message:
                        error_message = "Email already registered."
                    elif 'run' in error_message:
                        error_message = "RUN already registered."
                else:
                    error_message = 'An unexpected error has ocurred. Try again later.'
                return render(request, 'usermgr.html', {'error': error_message})
        elif 'login' in request.POST:
            email = request.POST['login_email']
            password = request.POST['login_password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    return redirect('usermgr')
                else:
                    return render(request, 'usermgr.html', {'error': 'Invalid Login'})
            except User.DoesNotExist:
                return render(request, 'usermgr.html', {'error': 'Invalid Login'})
    return render(request, 'usermgr.html')

def logout_view(request):
    logout(request)
    return redirect('usermgr')



@login_required
@user_passes_test(is_staff_user, login_url='/login/')
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


