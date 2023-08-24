from django.contrib.auth import views
from django.urls import path, include
from clients.views import ClientProfile, RegisterClient

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', ClientProfile.as_view(), name='clients.profile'),
    path('register/', RegisterClient.as_view(), name='clients.register'),
]