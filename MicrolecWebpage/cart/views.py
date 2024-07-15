from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .cartactions import CartAction
from product_management.models import Product

def index(request):
    return render(request, 'cart.html')

@login_required
def add_to_cart(request, product_id):
    product_instance = get_object_or_404(Product, pk=product_id)
    user_instance = request.user
    
    cart_item = CartAction.add_cart_item(product_instance, user_instance)
    
    return redirect('cart')
 