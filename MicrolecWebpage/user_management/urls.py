# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.usermgr, name='auth_view'),
    path('logout/', logout_view, name='logout'),
]
