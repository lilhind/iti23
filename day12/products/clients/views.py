from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from clients.forms import ModifiedUserForm

class ClientProfile(View):
    def get(self, request):
        return HttpResponse("Client Profile")
    

class RegisterClient(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/clients/login/'
    form_class = ModifiedUserForm
    
