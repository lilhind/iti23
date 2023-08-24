from django.urls import path, include

from .views import helloworld, secondRoot

urlpatterns = [
    path('', helloworld, name='helloworld'),
    path('2', secondRoot, name='secondRoot')
]