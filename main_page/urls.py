from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('post/<int:post_id>/',views.post_show,name = 'curr_post')
]
