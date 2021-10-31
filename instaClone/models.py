from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
Gender = (
  ('Male', 'Male'),
  ('Female', 'Female'),
)
class Location(models.Model):
  location = models.CharField(max_length=100)

  def saveLocation(self):
    self.save()

  @classmethod
  def deleteLocation(cls, id):
    cls.objects.filter(id=id).delete()

  @classmethod
  def updateLocation(cls, id, locaUpdate):
    cls.objects.filter(id=id).update(location=locaUpdate)

  def __str__(self):
    return self.location

class Profile(models.Model):
  propic = models.ImageField(upload_to='profiles/', null=True, blank=True, default='profiles/test.png')
  name= models.CharField(max_length=255, null=True)
  username = models.OneToOneField(User, on_delete=models.CASCADE)
  userbio = models.TextField()
  phoneNumber = models.IntegerField(null=True)
  gender = models.CharField(choices=Gender, default='Male', null=True, max_length=50)
  count = models.IntegerField(default=0, null=True, blank=True)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
      Profile.objects.create(username=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

  def __str__(self):
    return self.username.username

  @classmethod
  def searchProfile(cls, searchTerm):
    profiles = User.objects.filter(username__icontains=searchTerm)
    return profiles

