from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product
from django.shortcuts import get_object_or_404, redirect
from categories.models import Categories
from django.contrib.auth.decorators import login_required
# Create your views here.


# product (id , name , price , description , image , instock true/false , created_at , updated_at
productList = [
    {
        "id": 1,
        "name": "product1",
        "price": 100,
        "description": "this is product1",
        "image": "pic1.jpg",
        "instock": True,
        "created_at": "2021-10-10",
        "updated_at": "2021-10-10"
    },
    {
        "id": 2,
        "name": "product2",
        "price": 200,
        "description": "this is product2",
        "image": "pic2.jpg",
        "instock": True,
        "created_at": "2021-10-10",
        "updated_at": "2021-10-10"
    },
    {
        "id": 3,
        "name": "product3",
        "price": 300,
        "description": "this is product3",
        "image": "pic3.jpg",
        "instock": True,
        "created_at": "2021-10-10",
        "updated_at": "2021-10-10"
    }
]

def product(request):
    allProducts = Product.objects.all()
    return render(request, 'product.html', context={"products": allProducts})

def show(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'show.html', context={"product": product})

@login_required(login_url='login')
def delete(request,id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product.product')

@login_required(login_url='login')
def createProduct(request):
    categories = Categories.get_all_categories()
    if request.method == 'POST':
        name = request.POST['name']
        price = 0
        if request.POST['price'] == '':
            price = 0
        else:
            price = request.POST['price']
        description = request.POST['description']
        image = None
        category = None
        if request.FILES:
            image = request.FILES['image']
        if 'category' in request.POST:
            category = Categories.get_specific_category(id=request.POST['category'],cls=Categories)
        in_stock = False
        if 'in_stock' in request.POST:
            in_stock = True
        product = Product()
        product.image = image
        product.category = category
        product.name = name
        product.price = price
        product.description = description
        product.in_stock = in_stock
        product.save()
        return redirect('product.product')
    
    return render(request, 'product/create.html', context={"categories": categories})


@login_required(login_url='login')
def editStudent(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        if 'image' in request.FILES:
            image = request.FILES['image']
            product.image = image
        in_stock = False
        if 'in_stock' in request.POST:
            in_stock = True
        product.name = name
        product.price = price
        product.description = description
        product.in_stock = in_stock
        product.save()
        return redirect('product.product')   
    return render(request, 'product/edit.html', context={"product": product})