from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloworld(request):
    return HttpResponse("root of conatct_us")

def secondRoot(request):
    return HttpResponse("second root of contact_us")