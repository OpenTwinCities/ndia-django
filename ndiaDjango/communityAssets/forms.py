from django import forms
from leaflet.forms.widgets import LeafletWidget
from communityAssets.models import Organization


class OrganizationForm(forms.ModelForm):
	
	class Meta:
		model = Organization
		fields = ('lat_lon_json','Org_address','Org_name')
		widgets = {'lat_lon_json' : LeafletWidget()}
	