# the api.py file
from communityAssets.models import Event, Organization
from tastypie import fields
from tastypie.resources import ModelResource


class Org_Resource(ModelResource):
	events = fields.ToManyField('communityAssets.api.Event_Resource',"events",related_name="Organization",full=True,null=True)
	class Meta:
		resource_name = "orgs"
		queryset = Organization.objects.all()
		allowed_methods = ['get']
		
		
		
class Event_Resource(ModelResource):
	organization = fields.ToOneField('communityAssets.api.Org_Resource',attribute="orgs",related_name="Event",full=True,null=True)
	class Meta:
		resource_name = "events"
		queryset = Event.objects.select_related('Organization').all()
		allowed_methods = ['get']
		filtering = {
			"event_time" : ('year','gte',),
			}
		
		
		
