from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Comments

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
  
  class Meta:
    model = Profile
    exclude = ('username','count')
    fields = ('name', 'userbio', 'propic', 'phoneNumber', 'gender')
  
class PostPicForm(forms.ModelForm):
