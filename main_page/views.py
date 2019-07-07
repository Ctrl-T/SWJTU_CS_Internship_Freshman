from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import post,userinfo,category
# Create your views here.

category_list = category.objects.all()

def index(request):
    post_list = post.objects.all()
    return render(request,'index.html',{'POST_LIST':post_list,'CATEGORY_LIST':category_list})

def post_show(request,post_id):
    post_to_show = post.objects.get(id=post_id)
    post_to_show.view_count+=1
    post_to_show.ranking+=1
    post_to_show.save()
    return render(request,'post.html',{'POST':post_to_show})

def post_sub(request):
    content=request.POST.get('content')
    summary = request.POST.get('summary')
    title=request.POST.get('title')
    categorys = category.objects.get(id=int(request.POST.get('category')))
    author = userinfo.objects.get(user__username=request.user)
    post.objects.create(
        title =  title,
        summary = summary,
        category = categorys,
        content =  content,
        view_count = 1,
        comment_count = 0,
        author = author,
        ranking = 1,
    )
    return HttpResponseRedirect("/")

def category_show(request,category_id):
    post_list = post.objects.filter(category__id=category_id)
    return render(request,'category.html',{'POST_LIST':post_list,'CATEGORY_LIST':category_list})