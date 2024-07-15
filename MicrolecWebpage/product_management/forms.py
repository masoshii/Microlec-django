from django import forms

class AddproductForm(forms.Form):
    addproduct_name = forms.CharField(max_length=200, required=True)
    addproduct_brand = forms.CharField(max_length=200, required=True)
    addproduct_stock = forms.IntegerField(required=True)
    addproduct_price = forms.IntegerField(required=True)
    addproduct_image = forms.ImageField(required=True)

class DeleteproductForm(forms.Form):
    deleteproduct_id = forms.IntegerField(required=True)

class AddbrandForm(forms.Form):
    addbrand_name = forms.CharField(max_length=200, required=True)

class DeletebrandForm(forms.Form):
    deletebrand_id = forms.IntegerField(required=True)

class AddcategoryForm(forms.Form):
    addcategory_name = forms.CharField(max_length=200, required=True)

class DeletecategoryForm(forms.Form):
    deletecategory_id = forms.IntegerField(required=True)

class AddcategoryproductForm(forms.Form):
    addcategoryproduct_cid = forms.IntegerField(required=True)
    addcategoryproduct_pid = forms.IntegerField(required=True)

class RemovecategoryproductForm(forms.Form):
    removecategoryproduct_cid = forms.IntegerField(required=True)
    removecategoryproduct_pid = forms.IntegerField(required=True)