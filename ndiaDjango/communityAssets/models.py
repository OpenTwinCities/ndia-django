from django.db import models
from djgeojson.fields import PointField

class Organization(models.Model):
	lat_lon_json = PointField()
	Org_address = models.CharField(max_length=240)
	Org_name = models.CharField(max_length = 100)
	
	def __str__(self):
		return str(self.Org_name)
	
class Event(models.Model):
	event_place = models.ForeignKey(Organization)
	event_name = models.CharField(max_length = 100)
	event_time = models.DateTimeField()
	
	def __str__(self):
		return str(self.event_name)+ " " + self.event_time.strftime("%a-%d-%b-%Y")
