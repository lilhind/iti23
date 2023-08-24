from django.urls import path

from product.views import product, show, delete, createProduct, editStudent

urlpatterns = [
    path('', product , name='product.product'),
    path('<int:id>', show , name='product.show'),
    path('<int:id>/delete', delete , name='product.delete'),
    path('create', createProduct , name='product.create'),
    path('<int:id>/edit', editStudent , name='product.edit'),
]