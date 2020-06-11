from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .models import Profile

# Create your views here.


def user_profile_view(request):
    if request.user.is_authenticated:
        u = Profile.objects.get(uid_id=request.user)
        profileform = ProfileForm(instance=request.user)
        uprofile = UserProfileForm(instance=u)
        #profileform = ProfileForm(initial={'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email': request.user.email})
        #userprofile=UserProfileForm(initial={'gender':uprofile.gender,'phonenumber':uprofile.phonenumber})
        if request.method == 'POST':
            profileform = ProfileForm(request.POST, instance=request.user)
            uprofile = UserProfileForm(
                request.POST, request.FILES, instance=u)
                
            if uprofile.is_valid() and profileform.is_valid():
                uprofile.save()
                profileform.save()
                messages.info(request,f'Your account has been updated')
                return redirect('profile')
        return render(request, 'user/user_profile.html', {'context': profileform, 'profile': uprofile, 'username': request.user.username})

    else:
        return render(request, '404.html')


def logout_view(request):
    logout(request)
    return redirect('login')
