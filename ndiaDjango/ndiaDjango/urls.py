from django.conf.urls import patterns, include, url
from django.contrib import admin
from communityAssets.api import Event_Resource, Org_Resource


event_resource_api = Event_Resource(api_name = 'v1')
org_resource_api = Org_Resource(api_name = 'v1')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ndiaDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include(event_resource_api.urls)),
	url(r'^api/', include(org_resource_api.urls)),
	)