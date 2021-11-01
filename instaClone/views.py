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
def userprofile(request, id):
  try:
    user = Profile.objects.get(id = id)
    user_pics = Post.user_pictures(user.username)
    followers = User.objects.get(username = request.user.username).follower.all()
    
    foll_list = [follower.following.id for follower in followers]
    if request.user.id in foll_list:
      is_following = True
    else:
      is_following = False
    if request.user.username == str(user.username):
      return redirect('profile')
    else:
      using_user = User.objects.get(username = user.username)
      return render(request, 'otherUser.html', {'using_user': using_user,'userprofile':user, 'user_pics':user_pics, "is_following": is_following})
  except Profile.DoesNotExist:
    return HttpResponseRedirect(", Page Doesn't Exist")

def searchUser(request):
  if 'search' in request.GET and request.GET['search']:
    search_term = request.GET.get('search')
    searchprofiles = Profile.searchProfile(search_term)
    return render(request, 'search.html', {'searchresults':searchprofiles})
  else:
    return redirect('home')
def imagedetails(request, id):
  if request.method == 'POST':
    commentform = CommentForm(request.POST)
    if commentform.is_valid():
      photoId = int(request.POST.get('imageid'))
      photo = Post.objects.get(id=photoId)
      comment = commentform.save(commit=False)
      comment.user = request.user
      comment.pic = photo
      comment.save()
    return redirect('imagedetails', id=id)

  commentform = CommentForm(request.POST)
  pic = Post.objects.get(id = id)
  allcomments = Comments.objects.all()
  return render(request, 'imagedetails.html', {'photo':pic, 'commentform':commentform, 'allcomments':allcomments})

def post_photo(request):
  if request.method == 'POST':
    postForm = PostPicForm(request.POST, request.FILES)
    if postForm.is_valid():
      pic = postForm.save(commit=False)
      pic.uploadedBy = request.user
      pic.save()
    return redirect('profile')

  postForm = PostPicForm()
  return render(request, 'postphoto.html', {'postForm':postForm, 'user':request.user})

