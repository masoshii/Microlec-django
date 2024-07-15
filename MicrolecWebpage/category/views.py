from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from product_management.models import Product, Product_Category, Brand, Category

def product_list(request, category_name):
    category = Category.objects.get(name_category=category_name)
    
    product_categories = Product_Category.objects.filter(id_category=category)
    products = Product.objects.filter(id_product__in=[pc.id_product.id_product for pc in product_categories])
    
    order_by = request.GET.get('orderby', 'name_product')
    direction = request.GET.get('direction', 'asc')
    
    if direction == 'desc':
        order_by = f'-{order_by}'
    
    products = products.order_by(order_by)

    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'products': products,
        'page_obj': page_obj,   
    }
    return render(request, 'product_list.html', context)

def index(request):
    return redirect('index')