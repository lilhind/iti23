from django.urls import path

from .views import get_product, products_root

urlpatterns = [
    path('', products_root, name='products_root'),
    path('<int:product_id>', get_product, name='get_product'),
]