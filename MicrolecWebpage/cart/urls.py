from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="cart"),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]