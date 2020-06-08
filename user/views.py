from .forms import ProfileForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.


def user_profile_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        profileform = ProfileForm(
            initial={'first_name': user.first_name,
             'last_name': user.last_name, 'email': user.email})
            
        return render(request, 'user/user_profile.html', {'context': profileform,'username':user.username})

    else:
        return render(request, '404.html')


def logout_view(request):
    logout(request)
    return redirect('login')
