from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms
from django.contrib.auth import authenticate


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
        class Meta:
            model = User
            fields = ('email', 'first_name', 'last_name', 'password',)


