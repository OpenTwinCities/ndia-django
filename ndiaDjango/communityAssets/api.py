# the api.py file
from communityAssets.models import Event
from tastypie.resources import ModelResource



class Event_Resource(ModelResource):
	class Meta:
		resource_name = "events"
		queryset = Event.objects.all()
		allowed_methods = ['get']


