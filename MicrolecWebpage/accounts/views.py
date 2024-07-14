from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from django.db import IntegrityError
from user_management.models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data['email_field']
                password = form.cleaned_data['password_field']
                user = User.objects.get(email=email)
                if user.check_password(password):
                    login(request, user)
                    return redirect('index')
                else:
                    return render(request, 'login.html', {'error': 'Los datos de inicio de sesión son incorrectos.'})
            except User.DoesNotExist:
                return render(request, 'login.html', {'error': 'Los datos de inicio de sesión son incorrectos.'})
            except Exception as e:
                return render(request, 'login.html', {'error': f'Se han encontrado los siguientes errores a la hora de obtener los datos enviados: {e}'})
        else:
            for field in form:
                print("Field Error:", field.name,  field.errors)
            return render(request, 'login.html', {'error': 'Error en los tipos de campos.'})

    return render(request, 'login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                names = form.cleaned_data['names_field']
                lnames = form.cleaned_data['lnames_field']
                run = form.cleaned_data['run_field']
                email = form.cleaned_data['email_field']
                password = form.cleaned_data['password_field']

                user = User.objects.create_user(email=email, password=password, names=names, lnames=lnames, run=run)

                login(request, user)
                return redirect('index')
            except IntegrityError as ie:
                error_message = str(ie)
                if 'unique constraint' in error_message.lower():
                    if 'email' in error_message:
                        error_message = "Este email ya esta registrado."
                    elif 'run' in error_message:
                        error_message = "Este RUN ya esta registrado."
                else:
                    error_message = 'Un error inesperado ha ocurrido, intentelo de nuevo mas tarde.'
                return render(request, 'usermgr.html', {'error': error_message})
            except Exception as e:
                return render(request, 'register.html', {'error': f'Se han encontrado los siguientes errores a la hora de ingresar los datos enviados: {e}'})
        else:
            for field in form:
                print("Field Error:", field.name,  field.errors)
            return render(request, 'register.html', {'error': 'Error en los tipos de campos.'})

    return render(request, 'register.html')

def accounts(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return redirect('login')
