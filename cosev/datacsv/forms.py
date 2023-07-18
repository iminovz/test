from django import forms
from .models import CsvFile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CsvForm(forms.ModelForm):
    class Meta:
        model = CsvFile
        fields = ['title', 'cover']