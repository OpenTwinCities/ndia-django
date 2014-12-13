from django.db import models
from jsonfield import JSONField


class Organization(models.Model):
	lat_lon_json = JSONField()
	Org_address = models.CharField(max_length=240)
	Org_name = models.CharField(max_length = 100)
	
	
class Event(models.Model):
	event_place = models.ForeignKey(Organization)
	event_name = models.CharField(max_length = 100)
	event_time = models.DateTimeField()

