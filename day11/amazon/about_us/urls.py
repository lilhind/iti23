from django.urls import path

from .views import aboutUs1, aboutUs2

urlpatterns = [
    path('', aboutUs1, name='about_us1'),
    path('about_us/1', aboutUs1, name='about_us1'),
    path('/about_us/2', aboutUs2, name='abkht_us2')
]