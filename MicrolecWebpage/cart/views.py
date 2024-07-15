from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .cartactions import CartAction
from .models import CartModel
from product_management.models import Product, Product_Category

@login_required
def index(request):
    user = request.user
    user_products = CartModel.objects.filter(id_user=user)

    total_quantity = sum(item.quantity for item in user_products)
    allproducts_price = sum(item.id_product.price_product * item.quantity for item in user_products)
    shipping_price = total_quantity * 537
    total_price = shipping_price + allproducts_price

    return render(request, 'cart.html', {
        'user_products': user_products,
        'total_quantity': total_quantity,
        'allproducts_price': allproducts_price,
        'shipping_price': shipping_price,
        'total_price': total_price,
    })

@login_required
def add_to_cart(request, product_id):
    product_instance = get_object_or_404(Product, pk=product_id)
    user_instance = request.user

    CartAction.add_cart_item(product_instance, user_instance)
    
    return redirect('cart')

@login_required
def remove_from_cart(request, product_id):
    product_instance = get_object_or_404(Product, pk=product_id)
    user_instance = request.user
    
    CartAction.remove_cart_item(product_instance, user_instance)
    
    return redirect('cart')

@login_required
def update_quantity(request, product_id):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        new_quantity = request.POST.get('new_quantity')
        if new_quantity is not None:
            product_instance = get_object_or_404(Product, pk=product_id)
            user_instance = request.user

            CartAction.update_item_quantity(product_instance, user_instance, new_quantity)

            return JsonResponse({'success': True})
    return JsonResponse({'success': False})
 