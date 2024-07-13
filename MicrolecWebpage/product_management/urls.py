from django.urls import path

from . import views

urlpatterns = [
    path('', views.testmanage, name="testmanage"),
    path('productlist/', views.productlist, name='productlist'),
    path('brandlist/', views.brandlist, name='brandlist'),
    path('categorylist/', views.categorylist, name='categorylist'),
    path('productcategorylist/', views.productcategorylist, name='productcategorylist'),
]
