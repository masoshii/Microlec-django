from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='category'),
    path('<str:category_name>/', views.product_list, name='product_list'),
]