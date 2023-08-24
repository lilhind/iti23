from django.db import models
from django.shortcuts import reverse, get_object_or_404
# Create your models here.

class Categories(models.Model):
    #  create new model for categories: category (id , name, info, image --> image field)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    info = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True,upload_to='categories/images', blank=True)
    
    def __str__(self) -> str:
       return f"{self.name}"
    
    @classmethod

    def get_all_categories(cls):
        return cls.objects.all()
    
    def get_image_url(self):
        print(type(self.image))
        return f"/media/{self.image}"
    
    
    def get_show_url(self):
        return reverse('categories.show', args=[self.id])
    
    def get_edit_url(self):
        return reverse('categories.edit', args=[self.id])

    @classmethod

    def get_all_categories(cls):
        return cls.objects.all()
    
    def get_specific_category(cls, id):
        return get_object_or_404(cls, id=id)
    
