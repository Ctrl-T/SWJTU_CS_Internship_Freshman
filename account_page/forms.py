from django import forms
from django.contrib.auth.models import User
import re

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username',max_length=32)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)