from django.db import models
from djgeojson.fields import PointField

class Organization(models.Model):
	lat_lon_json = PointField()
	Org_address = models.CharField(max_length=240)
	Org_name = models.CharField(max_length = 100)
	def __str__(self):
		return "{0} {1}".format(self.Org_name,self.Org_address)
	
class Event(models.Model):
	event_place = models.ForeignKey(Organization,related_name='events')
	event_name = models.CharField(max_length = 100)
	event_time = models.DateTimeField()
	
	def __str__(self):
		return "{0} {1}".format(str(self.event_name),self.event_time.strftime("%a-%d-%b-%Y"))
