from django.test import TestCase
from .models import Location, Profile, Post
from django.contrib.auth.models import User


class TestLocation(TestCase):
  def setUp(self):
    self.location = Location(location='Kisumu')
    self.location.save()

  def TearDown(self):
    Location.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.location, Location))

  def test_saveLocation(self):
    self.location.save()
    location = Location.objects.all()
    self.assertTrue(len(location)>0)

  def test_deleteLocation(self):
    self.location.saveLocation()
    self.location2 = Location.objects.create(location='Kisii')
    Location.deleteLocation(self.location2.id)
    self.assertTrue(len(Location.objects.all())==1)

  def test_updateLocation(self):
    update_term = 'Kisii'
    self.location.saveLocation()
    Location.updateLocation(self.location.id, update_term)  
    updated_one = Location.objects.get(id=self.location.id)
    self.assertEqual(updated_one.location, 'Kisii')

class TestProfile(TestCase):
  def setUp(self):
    self.new_user = User(username = "nyotafloice", email = "nyotafloice@gmail.com",password = "nyotafloice1234")
    self.new_user.save()

  def tearDown(self):
    Profile.objects.all().delete()
    User.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.new_user.profile, Profile))

  def test_searchProfile(self):
    search = 'nyotafloice'
    self.new_user2 = User(username = "johndoe", email = "johndoe@gmail.com",password = "johndoe1234")
    self.new_user2.save()
    image_search = Profile.searchProfile(search)
    self.assertTrue(len(image_search) == 1)

class TestPost(TestCase):
  def setUp(self):
    self.location = Location(location='Machakos')
    self.location.save()
    self.new_user = User(username = "layersony")
    self.new_user.save()
    self.new_post = Post(picture='test.jpg',caption = 'this is trial' , uploadedBy = self.new_user, location=self.location)
    self.new_post.save_picture()
  
  def tearDown(self):
    Post.objects.all().delete()
    User.objects.all().delete()
    Location.objects.all().delete()

  def test_isinstance(self):
    self.assertTrue(isinstance(self.new_post, Post))

  def test_savePicture(self):
    self.new_post2 = Post(picture='test2.jpg',caption = 'amazing' , uploadedBy = self.new_user, location=self.location)
    self.new_post2.save_picture()
    self.assertEqual(len(Post.objects.all()),2)

  def test_deletePicture(self):
    self.new_post2 = Post(picture='test2.jpg',caption = 'amazing' , uploadedBy = self.new_user, location=self.location)
    self.new_post2.save_picture()
    self.assertEqual(len(Post.objects.all()),2)
    Post.delete_picture(self.new_post2.id)
    self.assertEqual(len(Post.objects.all()),1)

  def test_update(self):
    self.new_post.save_picture()
    self.new_post.update_caption(self.new_post.id, 'wow this is mmmmh.....')
    updated_post = Post.objects.get(id=self.new_post.id)
    self.assertEqual(updated_post.caption, 'wow this is mmmmh.....')   
  
  def test_allpics(self):
    self.new_post2 = Post(picture='test2.jpg',caption = 'amazing' , uploadedBy = self.new_user, location=self.location)
    self.new_post2.save_picture()
    self.assertEqual(len(Post.all_pictures()), 2)

  def test_userPictures(self):
    self.new_post2 = Post(picture='test2.jpg',caption = 'amazing' , uploadedBy = self.new_user, location=self.location)
    self.new_post2.save_picture()
    usrpic = Post.user_pictures(self.new_user.username)
    self.assertEqual(len(usrpic), 2)
