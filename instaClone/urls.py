from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='home'),
  path('profile/', views.currProfile, name='profile'),
  path('otherUser/<int:id>', views.otherUser, name='userprofile'),
  path('search/', views.searchUser, name='search_results'),
  path('imagedetails/<int:id>', views.imagedetails, name='imagedetails'),
  path('postphoto/', views.post_photo, name='postphoto'),
]
