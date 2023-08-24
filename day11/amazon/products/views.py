from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

products = [
    {
        'id': 1,
        'name': 'product1',
        'price': 100,
        'description': 'this is product1'
    },
    {
        'id': 2,
        'name': 'product2',
        'price': 200,
        'description': 'this is product2'
    },
    {
        'id': 3,
        'name': 'product3',
        'price': 300,
        'description': 'this is product3'
    },
]

def get_product(request, product_id):
    for product in products:
        if product['id'] == product_id:
            details = f"<p>name: {product['name']}</p><p>price: {product['price']}</p><p>description: {product['description']}</p>"
            return HttpResponse(details)
    return HttpResponse("product not found")

def products_root(request):
    return HttpResponse(products)