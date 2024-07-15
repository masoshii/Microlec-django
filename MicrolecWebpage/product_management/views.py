from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Brand, Product, Category, Product_Category
from .forms import AddproductForm, DeleteproductForm, AddbrandForm, DeletebrandForm, AddcategoryForm, DeletecategoryForm, AddcategoryproductForm, RemovecategoryproductForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .productsmanagement import ProductManager

def is_staff_user(user):
    return user.is_staff


@login_required
@user_passes_test(is_staff_user, login_url='login')
def productlist(request):
    model = Product.objects.all()
    data = list(model.values())
    return JsonResponse(data, safe=False)


@login_required
@user_passes_test(is_staff_user, login_url='login')
def brandlist(request):
    model = Brand.objects.all()
    data = list(model.values())
    return JsonResponse(data, safe=False)


@login_required
@user_passes_test(is_staff_user, login_url='login')
def categorylist(request):
    model = Category.objects.all()
    data = list(model.values())
    return JsonResponse(data, safe=False)


@login_required
@user_passes_test(is_staff_user, login_url='login')
def productcategorylist(request):
    model = Product_Category.objects.all()
    data = list(model.values())
    return JsonResponse(data, safe=False)

@login_required
@user_passes_test(is_staff_user, login_url='login')
def testmanage(request):
    if request.method == 'POST':
        if 'addproduct_form' in request.POST:
            form = AddproductForm(request.POST, request.FILES)
            if form.is_valid():
                product_name = form.cleaned_data['addproduct_name']
                product_brand = form.cleaned_data['addproduct_brand']
                product_stock = form.cleaned_data['addproduct_stock']
                product_price = form.cleaned_data['addproduct_price']
                product_image = request.FILES.get('addproduct_image')

                djangoresponse = ProductManager.addproduct(product_name, product_brand, product_stock, product_price, product_image)
                return render(request, 'productmgr.html', {'message':djangoresponse[1]})
            else:
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                return render(request, 'productmgr.html', {'message':'Error en los tipos de datos.'})
        elif 'deleteproduct_form' in request.POST:
            form = DeleteproductForm(request.POST)
            if form.is_valid():
                product_id = form.cleaned_data['deleteproduct_id']
                djangoresponse = ProductManager.deleteproduct(product_id)
                return render(request, 'productmgr.html', {'message':djangoresponse[1]})
            else:
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                return render(request, 'productmgr.html', {'message':'Error en los tipos de datos.'})
        elif 'addbrand_form' in request.POST:
            form = AddbrandForm(request.POST)
            if form.is_valid():
                brand_name = form.cleaned_data['addbrand_name']
                djangoresponse = ProductManager.addbrand(brand_name)
                return render(request, 'productmgr.html', {'message':djangoresponse[1]})
            else:
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                return render(request, 'productmgr.html', {'message':'Error en los tipos de datos.'})
        elif 'deletebrand_form' in request.POST:
            form = DeletebrandForm(request.POST)
            if form.is_valid():
                brand_id = form.cleaned_data['deletebrand_id']
                djangoresponse = ProductManager.deletebrand(brand_id)
                return render(request, 'productmgr.html', {'message':djangoresponse[1]})
            else:
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                return render(request, 'productmgr.html', {'message':'Error en los tipos de datos.'})
        elif 'addcategory_form' in request.POST:
            form = AddcategoryForm(request.POST)
            if form.is_valid():
                category_name = form.cleaned_data['addcategory_name']
                djangoresponse = ProductManager.addcategory(category_name)
                return render(request, 'productmgr.html', {'message':djangoresponse[1]})
            else:
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                return render(request, 'productmgr.html', {'message':'Error en los tipos de datos.'})
        elif 'deletecategory_form' in request.POST:
            form = DeletecategoryForm(request.POST)
            if form.is_valid():
                category_id = form.cleaned_data['deletecategory_id']
                djangoresponse = ProductManager.deletecategory(category_id)
                return render(request, 'productmgr.html', {'message':djangoresponse[1]})
            else:
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                return render(request, 'productmgr.html', {'message':'Error en los tipos de datos.'})
        elif 'addcategoryproduct_form' in request.POST:
            form = AddcategoryproductForm(request.POST)
            if form.is_valid():
                category_id = form.cleaned_data['addcategoryproduct_cid']
                product_id = form.cleaned_data['addcategoryproduct_pid']
                djangoresponse = ProductManager.addcategorytoproduct(product_id, category_id)
                return render(request, 'productmgr.html', {'message':djangoresponse[1]})
            else:
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                return render(request, 'productmgr.html', {'message':'Error en los tipos de datos.'})
        elif 'removecategoryproduct_form' in request.POST:
            form = RemovecategoryproductForm(request.POST)
            if form.is_valid():
                category_id = form.cleaned_data['removecategoryproduct_cid']
                product_id = form.cleaned_data['removecategoryproduct_pid']
                djangoresponse = ProductManager.removecategoryfromproduct(product_id, category_id)
                return render(request, 'productmgr.html', {'message':djangoresponse[1]})
            else:
                for field in form:
                    print("Field Error:", field.name,  field.errors)
                return render(request, 'productmgr.html', {'message':'Error en los tipos de datos.'})

    return render(request, 'productmgr.html')



