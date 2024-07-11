from django import forms

class ContactForm(forms.Form):
    name_field = forms.CharField(max_length=200, required=True)
    lastnames_field = forms.CharField(max_length=200, required=True)
    email_field = forms.EmailField()
    comment_field = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':10}), max_length=2000)
