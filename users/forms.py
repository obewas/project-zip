from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Project


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
  
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
  
  
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
  
    class Meta:
        model = User
        fields = ['username', 'email']
  
  
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture','bio', 'location', 'contact']

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

