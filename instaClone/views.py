from django.shortcuts import redirect, render
from instaClone.forms import CommentForm
from .models import Post, Profile, Location, Comments

def index(request):
  if request.method == 'POST':
    commentform = CommentForm(request.POST)
    if commentform.is_valid():
      photoId = int(request.POST.get('imageid'))
      photo = Post.objects.get(id=photoId)

      comment = commentform.save(commit=False)
      comment.user = request.user
      comment.pic = photo
      comment.save()
    return redirect('/#image'+str(photoId))

  allusers = Profile.objects.all()
  allpictures = Post.all_pictures()
  commentform = CommentForm()
  allcomments = Comments.objects.all()
  content = {
    'allpictures':allpictures,
    'allusers': allusers,
    'commentform':commentform,
    'allcomments':allcomments
  }
  return render(request, 'index.html', content)

def currProfile(request):
  content={

  }
  return render(request, 'currprofile.html', content)