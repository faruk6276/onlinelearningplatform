from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,PasswordResetForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib.sites.shortcuts import get_current_site 
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import View
from django.contrib import messages
import json
import requests
# Create your views here.




#Login Function
def login(request):
    loginForm= LoginForm()
    if request.method=='POST':
        client_key = request.POST.get('g-recaptcha-response')
        secret_key = '6LcdJAAVAAAAAF2t7rVKW3uk4C-uVq8VbBOodrI7'
        captchadata={
            'secret':secret_key,
            'response':client_key
        }
        r = requests.post(' https://www.google.com/recaptcha/api/siteverify', data=captchadata)
        response=json.loads(r.text)
        verify=response['success']
        print(verify)
        if verify==True:
            loginForm=LoginForm(request.POST)
            if loginForm.is_valid():
                username=loginForm.cleaned_data['username']
                password=loginForm.cleaned_data['password']
                
                user=auth.authenticate(username=username,password=password)
                if user is not None:
                    auth.login(request,user)
                    return redirect("/")
                else:
                    messages.info(request, 'Invalid Username Or Password')
        else:
            messages.info(request, 'Please confirm you are not a robot')
    return render(request, 'login.html',{'context': loginForm})




#Registration Function
def register(request):
    my_form = RegisterForm()
    if request.method=='POST':
        my_form = RegisterForm(request.POST)
        if my_form.is_valid():
            uname=my_form.cleaned_data['username']
            fname=my_form.cleaned_data['first_name']
            lname=my_form.cleaned_data['last_name']
            email=my_form.cleaned_data['email']
            password=my_form.cleaned_data['password']
            confirm_password=my_form.cleaned_data['confirm_password']
            
            if User.objects.filter(username=uname).exists():
                print("ok0")
                messages.info(request, 'Username already exist')
            elif User.objects.filter(email=email).exists():
                print("ok1")
                messages.info(request, 'Your email already a registered')
            else:
                print("ok2")
                user=User.objects.create_user(username=uname,password=password,first_name=fname,last_name=lname,email=email)
                user.is_active=False
                user.save()
                print('User created')

                #return redirect('/')
                current_site=get_current_site(request)
                email_subject='Activate Your Account',
                message=render_to_string('activate.html',
                {
                    'user':user,
                    'domain':current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':generate_token.make_token(user)
                })
                email_message = EmailMessage(
                    email_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                email_message.send()
                return render(request,'registration_done.html')

    #context={'form':form}
    return render(request, 'register.html', {'context': my_form})





#New user activation function
def ActivateAccountView(request,uidb64,token, *args, **kwargs):
    try:
        uid=force_text(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except Exception as idetifier:
        user=None
       
    if user is not None and generate_token.check_token(user,token):
        user.is_active=True
        user.save()
        return render(request, 'useractivationdone.html')

    else:
        return render(request, '404.html')
 




def resetpass(request):
    reset=PasswordResetForm()
    if request.method == 'POST':
        reset = PasswordResetForm(request.POST)
        if reset.is_valid():
            email = reset.cleaned_data['email']
            try:
                user=User.objects.get(email=email)
                print(user.username)
            except Exception as idetifier:
                user = None
            if user is not None:
                print('ok0')
                current_site = get_current_site(request)
                email_subject = 'Reset Your password',
                
                message = render_to_string('resetpassemail.html',
                                           {
                                               'user': user,
                                               'domain': current_site.domain,
                                               'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                               'token': generate_token.make_token(user)
                                           })
                print('ok1')
                email_message = EmailMessage(
                    email_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                email_message.send()
                print('ok2')
        return redirect('resetdone')

    return render(request, 'resetpass.html',{'context': reset})





def resetpassconf(self, uidb64, token, *args, **kwargs):
    return redirect('resetdone')


def resetdone(request):
    return render(request, 'sendconfresetpass.html')


def sendconfresetpass(request):
    return render(request, 'sendconfresetpass.html')
