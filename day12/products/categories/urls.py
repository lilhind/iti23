from django.urls import path
from categories.views import CreateCategoy, ListCategories, DeleteCategory, EditCategory, CreateCategoryGN, ListCategoryGN, DeleteCategoryGN, EditCategoryGN, ShowCategoryGN
from django.contrib.auth.decorators import login_required

from categories.views import index, show, create_via_model, delete, edit
urlpatterns = [
    path('', ListCategoryGN.as_view() , name='categories.index'),
    #path('', ListCategories.as_view() , name='categories.index'),
    #path('', index , name='categories.index'),
    path('<int:pk>', ShowCategoryGN.as_view() , name='categories.show'),
    #path('<int:id>', show , name='categories.show'),
    path('create', login_required(CreateCategoryGN.as_view(), login_url="/clients/login/") , name='categories.create'),
    #path('create', CreateCategoy.as_view() , name='categories.create'),
    #path('create', create_via_model , name='categories.create'),
    path('delete/<int:pk>', login_required(DeleteCategoryGN.as_view(), login_url="/clients/login/") , name='categories.delete'),
    #path('delete/<int:id>', DeleteCategory.as_view() , name='categories.delete'),
    #path('delete/<int:id>', delete , name='categories.delete'),
    
    path('edit/<int:pk>', login_required(EditCategoryGN.as_view(), login_url="/clients/login/") , name='categories.edit'),
    #path('edit/<int:id>', EditCategory.as_view() , name='categories.edit'),
    #path('edit/<int:id>', edit , name='categories.edit'),
]