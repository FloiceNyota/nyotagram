from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='home'),
  path('imagedetails/<int:id>', views.imagedetails, name='imagedetails'),
]
