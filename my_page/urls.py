from django.urls import path
from . import views

urlpatterns = [
    path('<name>/',views.homepage_show)
]