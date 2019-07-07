from django.shortcuts import render,get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from main_page.models import userinfo
from .forms import RegistrationForm,LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['cf_password']
            name=form.cleaned_data['name']
            college=form.cleaned_data['college']
            department=form.cleaned_data['department']
            classinfo=form.cleaned_data['classinfo']
            user = User.objects.create_user(username=username,password=password,email=email)
            userinfo.objects.create(
                user=user,
                name=name,
                college=college,
                department=department,
                classinfo=classinfo
            )
            return HttpResponseRedirect("/account/login/")      
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username,password=password)

            if user is not None and user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect("/")
            else:
                return render(request,'login.html',{'form':form,'message':'密码或用户名错误'})
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
