from django.forms import ModelForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django import forms

class EditUserDetailsForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

