from django.contrib import admin
from communityAssets.models import Event, Organization
from communityAssets.forms import OrganizationForm
from leaflet.admin import LeafletGeoAdmin

#change the admin site header title

admin.site.site_header = 'NDIA Community Assets Site'

#The next two lines register the 2 models that we have
admin.site.register(Event)
admin.site.register(Organization, LeafletGeoAdmin)


