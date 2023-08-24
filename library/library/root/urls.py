
from django.urls import path
from django.contrib.auth.decorators import login_required
from root.views import root
from django.shortcuts import render, redirect

urlpatterns = [
    path('', root, name='root'),    
]