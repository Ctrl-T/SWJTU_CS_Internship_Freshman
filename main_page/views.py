from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import post
# Create your views here.

post_list = post.objects.all()
def index(request):
    return render(request,'index.html',{'POST_LIST':post_list})

def post_show(request,post_id):
    post_to_show = post.objects.get(id=post_id)
    return render(request,'post.html',{'POST':post_to_show})