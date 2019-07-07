from django.shortcuts import render,get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from main_page.models import userinfo
from .forms import RegistrationForm,LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['cf_password']
            users = User.objects.create_user(username=username,password=password,email=email)
            user_profile = userinfo(user=users)
            user_profile.save()
        return HttpResponseRedirect("/")
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def login(request):
    pass

def logout(request):
    pass
