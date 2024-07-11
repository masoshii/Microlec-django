from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.http import JsonResponse
from .forms import ContactForm
from .models import ContactModel
import math

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            try:
                name = form.cleaned_data['name_field']
                lastnames = form.cleaned_data['lastnames_field']
                email = form.cleaned_data['email_field']
                comment = form.cleaned_data['comment_field']
                ip = request.META.get('REMOTE_ADDR', None)
            except Exception as e:
                return HttpResponse(f'Se han encontrado los siguientes errores a la hora de obtener los datos enviados: {e}')


            try:
                if ContactModel.objects.filter(ip_contact=ip).exists():
                    now_date = timezone.now()
                    recent_data = ContactModel.objects.filter(ip_contact=ip).latest('timestamp_contact')
                    recent_timestamp = recent_data.timestamp_contact
                    time_diff = now_date.replace(tzinfo=None) - recent_timestamp.replace(tzinfo=None)
                    if time_diff.total_seconds() < 60:
                        return HttpResponse(f'Muchas solicitudes, espere {math.trunc(60 - time_diff.total_seconds())} segundos e intentelo de nuevo.')
                    pass
            except Exception as e:
                return HttpResponse(f'Se han encontrado los siguientes errores a la hora de procesar los datos enviados: {e}')
            
            try:
                new_data_insert = ContactModel(
                    name_contact = name,
                    lastnames_contact = lastnames,
                    email_contact = email,
                    comment_contact = comment,
                    timestamp_contact = timezone.now(),
                    ip_contact = ip
                )

                new_data_insert.save()

            except Exception as e:
                return HttpResponse(f"Se han encontrado los siguientes errores a la hora de ingresar los datos en el sistema: {e}")

            return HttpResponse(f'Se envio con los siguientes datos: {name}, {lastnames}, {email}, {comment}, {ip}')
        else:
            for field in form:
                print("Field Error:", field.name,  field.errors)
    return render(request, 'contact.html')

def allcontact(request):


    contact_list = ContactModel.objects.all()
    data = list(contact_list.values())

    return JsonResponse(data, safe=False)
