from django.db import models
from django.shortcuts import reverse
from categories.models import Categories

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, related_name='products')
    
    #def __str__(self) -> str:
    #    return self.name
    
    def get_edit_url(self):
        return reverse('product.edit', args=[self.id])
    
    def get_show_url(self):
        return reverse('product.show', args=[self.id])
    
    def get_img_url(self):
        if not self.image:
            return None
        return self.image.url