from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='home'),
  path('otherUser/<int:id>', views.otherUser, name='userprofile'),
  path('imagedetails/<int:id>', views.imagedetails, name='imagedetails'),
]
