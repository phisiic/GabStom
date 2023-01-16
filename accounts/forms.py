from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import User, DoKontaktu
from django import forms
from django.contrib.auth import authenticate


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2',)


class CustomUserChangeForm(UserChangeForm):
        class Meta:
            model = User
            fields = ('email', 'first_name', 'last_name', 'password',)


class ContactForm(ModelForm):
    class Meta:
        model = DoKontaktu
        fields = ('email',)


