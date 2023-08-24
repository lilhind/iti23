from django.db import models
from django.shortcuts import reverse, get_object_or_404, render
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
#Create your models here.
#class Students(models.Model):
#    student_name = models.CharField(max_length=100)
#    student_email = models.EmailField()
#    student_password = models.CharField(max_length=100)
#    student_image = models.ImageField(upload_to='students/', null=True, blank=True)
#
#    def __str__(self):
#        return self.student_name
#
#    def get_absolute_url(self):
#        return reverse('student:student_detail', kwargs={'pk': self.pk})
#

class Students(User):
    #student_id = models.AutoField(primary_key=True)
    USERNAME_FIELD = 'username'
    user_ptr = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True, related_name='student', null=False, blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password']

class StudentCreationForm(UserCreationForm):
    class Meta:
        model = Students
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')