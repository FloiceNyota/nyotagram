from django import forms
from django.contrib.auth.models import User
from django.db.models.fields import TextField
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
  class Meta:
    model = Post
    exclude = ('uploadedBy', 'posted')
    fields = '__all__'

class CommentForm(forms.ModelForm):
  comment = forms.CharField(required=True,  label='', widget=forms.TextInput(attrs={'class':'comment-box', 'placeholder':'Add a comment' , 'id':'comment', 'name':'comment'}))
  class Meta:
    model = Comments
    exclude = ('pic', 'user')
    fields = ['comment']
