from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Brand, Product, Category, Product_Category
from .forms import AddproductForm, DeleteproductForm, AddbrandForm, DeletebrandForm
from .productsmanagement import ProductManager


def productlist(request):
    model = Product.objects.all()
    data = list(model.values())
    return JsonResponse(data, safe=False)

def brandlist(request):
    model = Brand.objects.all()
    data = list(model.values())
    return JsonResponse(data, safe=False)

def categorylist(request):
    model = Category.objects.all()
    data = list(model.values())
    return JsonResponse(data, safe=False)

def productcategorylist(request):
    model = Product_Category.objects.all()
    data = list(model.values())
    return JsonResponse(data, safe=False)

def testmanage(request):
    if request.method == 'POST':
        if 'addproduct_form' in request.POST:
            form = AddproductForm(request.POST)
            if form.is_valid():
                product_name = form.cleaned_data['addproduct_name']
                product_brand = form.cleaned_data['addproduct_brand']
                product_stock = form.cleaned_data['addproduct_stock']
                product_price = form.cleaned_data['addproduct_price']
                djangoresponse = ProductManager.addproduct(product_name, product_brand, product_stock, product_price)
                return HttpResponse(djangoresponse[1])
            else:
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                return HttpResponse('Tipos de campo incorrectos.')
        elif 'deleteproduct_form' in request.POST:
            form = DeleteproductForm(request.POST)
            if form.is_valid():
                product_id = form.cleaned_data['deleteproduct_id']
                djangoresponse = ProductManager.deleteproduct(product_id)
                return HttpResponse(djangoresponse[1])
            else:
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                return HttpResponse('Tipos de campo incorrectos.')
        elif 'addbrand_form' in request.POST:
            form = AddbrandForm(request.POST)
            if form.is_valid():
                brand_name = form.cleaned_data['addbrand_name']
                djangoresponse = ProductManager.addbrand(brand_name)
                return HttpResponse(djangoresponse[1])
            else:
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                return HttpResponse('Tipos de campo incorrectos.')
        elif 'deletebrand_form' in request.POST:
            form = DeletebrandForm(request.POST)
            if form.is_valid():
                brand_id = form.cleaned_data['deletebrand_id']
                djangoresponse = ProductManager.deletebrand(brand_id)
                return HttpResponse(djangoresponse[1])
            else:
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                return HttpResponse('Tipos de campo incorrectos.')
        

    return render(request, 'productmgr.html')



