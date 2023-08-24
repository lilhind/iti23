from django.shortcuts import render, redirect
from categories.models import Categories
from django.http import HttpResponse
from categories.forms import CategoryForm, CategoryModelForm
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


def index(request):
    # get all categories
    allCategories = Categories.get_all_categories()
    return render(request, 'categories/index.html', context={"categories": allCategories})

def show(request, id):
    category = Categories.get_specific_category(cls=Categories,id=id)
    return render(request, 'categories/show.html', context={"category": category})

def create(request):
    form = CategoryForm()
    if request.method == 'POST':
        name = request.POST['name']
        info = request.POST['info']
        image = None
        if request.FILES:
            image = request.FILES['image']
        category = Categories.objects.create(name=name, info=info, image=image)
        return redirect('categories.index')

    return render(request, 'categories/create.html', context={"form": form})

def create_via_model(request):
    form = CategoryModelForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            category = form.save()
            #return HttpResponse(category.name)
            return redirect('categories.index')
        else:
            return HttpResponse("Form is not valid")
    return render(request, 'categories/create.html', context={"form": form})


def edit(request, id):
    category = Categories.get_specific_category(cls=Categories,id=id)
    form = CategoryModelForm(instance=category)
    if request.method == 'POST':
        form = CategoryModelForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('categories.index')
        else:
            return HttpResponse("Form is not valid")
    return render(request, 'categories/edit.html', context={"form": form})

def delete(request, id):
    category = Categories.get_specific_category(cls=Categories,id=id)
    category.delete()
    return redirect('categories.index')


class CreateCategoy(View):
    def get(self, request):
        form = CategoryModelForm()
        return render(request, 'categories/create.html', context={"form": form})
    
    def post(self, request):
        form = CategoryModelForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            return redirect('categories.index')
        else:
            return HttpResponse("Form is not valid")

class ListCategories(View):
    def get(self, request):
        allCategories = Categories.get_all_categories()
        return render(request, 'categories/index.html', context={"categories": allCategories})
    
class DeleteCategory(View):
    def get(self, request, id):
        category = Categories.get_specific_category(cls=Categories,id=id)
        category.delete()
        return redirect('categories.index')
    
class EditCategory(View):
    def get(self, request, id):
        category = Categories.get_specific_category(cls=Categories,id=id)
        form = CategoryModelForm(instance=category)
        return render(request, 'categories/edit.html', context={"form": form})
    
    def post(self, request, id):
        category = Categories.get_specific_category(cls=Categories,id=id)
        form = CategoryModelForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('categories.index')
        else:
            return HttpResponse("Form is not valid")
        

class CreateCategoryGN(CreateView):
    model = Categories
    fields = ['name', 'info', 'image']
    template_name = 'categories/create.html'
    success_url = '/categories'

class ListCategoryGN(ListView):
    model = Categories
    template_name = 'categories/index.html'
    context_object_name = 'categories'

class DeleteCategoryGN(DeleteView):
    model = Categories
    template_name = 'categories/delete.html'
    success_url = '/categories'

class EditCategoryGN(UpdateView):
    model = Categories
    fields = ['name', 'info', 'image']
    template_name = 'categories/edit.html'
    success_url = '/categories'

# add login required

class ShowCategoryGN(DetailView):
    model = Categories
    template_name = 'categories/show.html'
    context_object_name = 'category'

