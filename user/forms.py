from django import forms
from django.contrib.auth.models import User

class ProfileForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=30,
                                 required=True, widget=forms.TextInput(attrs={'class': 'input_field'}))
    last_name = forms.CharField(label="Last Name", max_length=30, required=True,
                                widget=forms.TextInput(attrs={'class': 'input_field'}))
    email = forms.EmailField(label="Email", required=True, widget=forms.TextInput(
        attrs={'class': 'input_field'}))
