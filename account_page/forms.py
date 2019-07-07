from django import forms
from django.contrib.auth.models import User
import re


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)

class RegistrationForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=32)
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
    cf_password = forms.CharField(label='确认密码', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email',max_length=32)
    name = forms.CharField(label='姓名',max_length=32)
    college = forms.CharField(label='学院',max_length=32)
    department = forms.CharField(label='专业',max_length=32)
    classinfo = forms.CharField(label='班级',max_length=32)
    def clean_username(self):
       username = self.cleaned_data.get('username')

       if len(username) < 1:
           raise forms.ValidationError("用户名不为空")
       elif len(username) > 32:
           raise forms.ValidationError("用户名太长")
       else:
           filter_result = User.objects.filter(username__exact=username)
           if len(filter_result) > 0:
               raise forms.ValidationError("用户名已存在")
       return username

    def clean_email(self):
       email = self.cleaned_data.get('email')

       if email_check(email):
           filter_result = User.objects.filter(email__exact=email)
           if len(filter_result) > 0:
               raise forms.ValidationError("电子邮箱已存在")
       else:
           raise forms.ValidationError("请输入合法邮箱")
       return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 6:
            raise forms.ValidationError("密码太短.")
        elif len(password) > 20:
            raise forms.ValidationError("密码太长.")
        return password

    def clean_cf_password(self):
        password = self.cleaned_data.get('password')
        cf_password = self.cleaned_data.get('cf_password')

        if password and cf_password and password != cf_password:
            raise forms.ValidationError("密码不匹配，请重新输入")
        return cf_password

class LoginForm(forms.Form):

    username = forms.CharField(label='用户名',max_length=32)
    password = forms.CharField(label='密码', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')          

        filter_result = User.objects.filter(username__exact=username)
        if not filter_result:
            raise forms.ValidationError("用户名不存在")
        return username