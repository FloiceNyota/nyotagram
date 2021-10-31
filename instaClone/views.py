from django.shortcuts import render
from .models import Post, Profile, Location, Comments

def index(request):
  allusers = Profile.objects.all()
  allpictures = Post.all_pictures()
  content = {
    'allpictures':allpictures,
    'allusers': allusers,
  }
  return render(request, 'index.html', content)