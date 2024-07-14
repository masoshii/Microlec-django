from django import forms

class LoginForm(forms.Form):
    email_field = forms.EmailField(required=True)
    password_field = forms.CharField(max_length=255, required=True)