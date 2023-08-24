from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def aboutUs1(request):
    return HttpResponse("about_us1")

def aboutUs2(request):
    return HttpResponse("about_us2")