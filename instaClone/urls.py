from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns = [
  path('', views.index, name='home'),
  path('profile/', views.currProfile, name='profile'),
  path('otherUser/<int:id>', views.otherUser, name='userprofile'),
  path('search/', views.searchUser, name='search_results'),
  path('imagedetails/<int:id>', views.imagedetails, name='imagedetails'),
  path('postphoto/', views.post_photo, name='postphoto'),
  path('ajax/follow/profile', views.followuser , name='followuser'),
  path('accounts/', include('django_registration.backends.one_step.urls')),
  path('accounts/', include('django.contrib.auth.urls')),
]
