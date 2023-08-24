from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.forms import RegisterationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import login
from student.models import Students
from django.contrib.auth import logout




class RegisterUser(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = "/user/login/"
    form_class = RegisterationForm

class RegisterStudent(CreateView):
    model = Students
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = "/user/login/"
    form_class = RegisterationForm

from django.shortcuts import redirect

def logout_view(request):
    pass