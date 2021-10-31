from django.test import TestCase
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

