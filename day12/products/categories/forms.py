from django import forms
from categories.models import Categories
class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100, label='Category Name')
    info = forms.CharField(widget=forms.Textarea, label='Category Info')
    image = forms.ImageField(label='Category Image', required=False)

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'
        labels = {
            'name': 'Category Name',
            'info': 'Category Info',
            'image': 'Category Image'
        }
        widgets = {
            'info': forms.Textarea(attrs={'rows': 5, 'cols': 20})
        }
