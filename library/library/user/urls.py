from django.contrib.auth import views
from django.urls import path, include
from .views import RegisterUser, RegisterStudent, logout_view

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterStudent.as_view(), name='user.register'),
    #path('register/', RegisterUser.as_view(), name='user.register'),
    #path('login/', loginview, name='user.login'),
    
]