from django import forms

class Register(forms.Form):
    fname = forms.CharField(max_length=30, required=True)
    lname = forms.CharField( max_length=30, required=True)
    email = forms.EmailField(required=True)
    pas = forms.CharField( max_length=30, required=True)
    rpas = forms.CharField(max_length=30, required=True)
