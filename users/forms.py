from django import forms
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input_field'}),
            'last_name': forms.TextInput(attrs={'class': 'input_field'}),
            'email': forms.TextInput(attrs={'class': 'input_field'}),
        }


class UserProfileForm(forms.ModelForm):
    """Form definition for MODELNAME."""
    class Meta:
        """Meta definition for MODELNAMEform."""
        
        model = Profile
        fields = ['phonenumber', 'gender', 'profile_picture']
        widgets={
            'phonenumber': forms.TextInput(attrs={'class': 'input_field'}),
        }
