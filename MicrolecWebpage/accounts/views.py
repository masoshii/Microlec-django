from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
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
                return HttpResponse(f'Se han encontrado los siguientes errores a la hora de obtener los datos enviados: {e}')
        else:
            for field in form:
                print("Field Error:", field.name,  field.errors)
            return HttpResponse('Tipos de campo incorrectos.')

    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def accounts(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return redirect('login')
