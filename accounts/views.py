from django.shortcuts import render
from .forms import Register
# Create your views here.


def login(request):
    return render(request, 'login.html')

def register(request):
    form=Register(request.POST or None)
    if form.is_valid():
        form.save()

    #context={'form':form}
    return render(request,'try.html', {'context':form})