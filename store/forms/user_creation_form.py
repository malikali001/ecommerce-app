from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from store.models.newuser import NewUser
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['username', 'first_name', 'last_name', 'email', 'image']

