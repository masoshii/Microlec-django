from django import forms

class LoginForm(forms.Form):
    email_field = forms.EmailField(required=True)
    password_field = forms.CharField(max_length=255, required=True)

class RegisterForm(forms.Form):
    names_field = forms.CharField(max_length=255, required=True)
    lnames_field = forms.CharField(max_length=255, required=True)
    run_field = forms.CharField(max_length=10, required=True)
    email_field = forms.EmailField(required=True)
    password_field = forms.CharField(max_length=255, required=True)
