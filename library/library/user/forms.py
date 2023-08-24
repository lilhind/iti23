from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from student.models import Students

class RegisterationForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True, help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.')
    # add first name and last name
    first_name = forms.CharField(max_length=20, required=True, help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.')
    last_name = forms.CharField(max_length=20, required=True, help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(max_length=20, required=True, help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.')
    password2 = forms.CharField(max_length=20, required=True, help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.')
    class Meta:
        model = Students
        fields = ('username', 'first_name', 'last_name' , 'email', 'password1', 'password2')


