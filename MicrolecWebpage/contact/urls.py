from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="contact"),
    path('success/', views.success, name='success'),
]