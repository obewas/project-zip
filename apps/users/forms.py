from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Project, Grading
from django.forms import ModelForm
from .models import Photo, Photo2, Photo3

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
        fields = ['picture','bio', 'location', 'contact','profession']

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'



class PhotoForm(ModelForm):
  class Meta:
      model = Photo
      fields = ['name', 'image']

class Photo2Form(ModelForm):
  class Meta:
      model = Photo2
      fields = ['name', 'image']
class Photo3Form(ModelForm):
  class Meta:
      model = Photo3
      fields = ['name', 'image']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grading
        fields=['design','content','usability','creativity']
