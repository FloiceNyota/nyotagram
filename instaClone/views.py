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
  if request.method == 'POST':
    userForm = UserForm(request.POST, instance=request.user)
    profileForm = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    if userForm.is_valid() and profileForm.is_valid():
      userForm.save()
      profileForm.save()
    return redirect('profile')

  userForm = UserForm(instance=request.user)
  profileForm = ProfileForm(instance=request.user)
  curruser_photos = Post.user_pictures(request.user.username)
  content={
    'userForm':userForm,
    'profileForm':profileForm,
    'curruser_photos':curruser_photos,
    'curruser':request.user,
  }
  return render(request, 'currprofile.html', content)