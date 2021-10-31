from django.shortcuts import render
from .models import Post, Profile, Location, Comments

def index(request):
  allpictures = Post.all_pictures()
  content = {
    'allpictures':allpictures,
  }
  return render(request, 'index.html', content)