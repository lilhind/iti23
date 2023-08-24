from django.db import models
from django.urls import reverse
from student.models import Students
from django.utils import timezone
from django.contrib import admin

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True, blank=True)
    picture = models.ImageField(null=True,upload_to='books/images', blank=True)
    price = models.IntegerField()
    summary = models.TextField(null=True, blank=True)
    publisher = models.CharField(max_length=100)
    pubdate = models.DateField()
    borrowed_by = models.ForeignKey(Students, on_delete=models.CASCADE, null=True, blank=True)
    borrow_date = models.DateField(null=True, blank=True)
    # create return date and set default to be 7 days from borrow date

    def return_date(self):
        return self.borrow_date + timezone.timedelta(days=7)
    
    def __str__(self) -> str:
       return f"{self.title}"
    
    def get_edit_url(self):
        return reverse('edit', kwargs={'pk': self.pk})
        return reverse('student.details', args=[self.id])
    
    @classmethod

    def get_image_url(self):
        print(type(self.picture))
        return f"/media/{self.picture}"
        
    def get_show_url(self):
        return reverse('student.details', args=[self.id])
    
    def get_all_books(cls):
        return cls.objects.all()
    
    def borrow_book(self, user_id):
        self.borrowed_by = user_id
        self.borrow_date = timezone.now()
        self.save()

