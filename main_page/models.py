# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User

class userinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    college = models.CharField(max_length=32)
    department = models.CharField(max_length=32)
    classinfo = models.CharField(max_length=32)
    photo = models.ImageField(upload_to='upload_imag/', default='upload_imag/default.png')
    signature = models.CharField(max_length=256,default='Hello World!')
    def __str__(self):
        return self.name


class post(models.Model):
    title =  models.CharField(max_length=64)
    summary = models.CharField(max_length=256,blank=True)
    category = models.CharField(max_length=32)
    content =  models.TextField()
    view_count = models.IntegerField()
    comment_count = models.IntegerField()
    author = models.ForeignKey('userinfo',on_delete=models.CASCADE)
    ranking = models.IntegerField()
    publish_date = models.DateTimeField()
    modify_date = models.DateTimeField()

    def __str__(self):
        return self.title


class category(models.Model):
    name = models.CharField(max_length=32,primary_key=True)
    admin = models.ForeignKey('userinfo',on_delete=models.CASCADE)
    def __str__(self):
        return self.name