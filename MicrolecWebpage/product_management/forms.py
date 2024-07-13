from django import forms

class AddproductForm(forms.Form):
    addproduct_name = forms.CharField(max_length=200, required=True)
    addproduct_brand = forms.CharField(max_length=200, required=True)
    addproduct_stock = forms.IntegerField(required=True)
    addproduct_price = forms.IntegerField(required=True)

class DeleteproductForm(forms.Form):
    deleteproduct_id = forms.IntegerField(required=True)

class AddbrandForm(forms.Form):
    addbrand_name = forms.CharField(max_length=200, required=True)

class DeletebrandForm(forms.Form):
    deletebrand_id = forms.IntegerField(required=True)