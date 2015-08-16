#from cl.search import api
#from cl.search import api2
from cl.search.feeds import (
    JurisdictionFeed, AllJurisdictionsFeed, SearchFeed
)

from django.conf.urls import include, url
from tastypie.api import Api

# Set up the API
#v1_api = Api(api_name='v1')
#v1_api.register(api.CitationResource(tally_name='search.api.citation'))
#v1_api.register(api.JurisdictionResource(tally_name='search.api.court'))
#v1_api.register(api.DocumentResource(tally_name='search.api.document'))
#v1_api.register(api.SearchResource(tally_name='search.api.search'))
#v1_api.register(api.CitesResource(tally_name='search.api.cites'))
#v1_api.register(api.CitedByResource(tally_name='search.api.cited-by'))
# v2_api = Api(api_name='v2')
# v2_api.register(api2.AudioResource(tally_name='search.ap2.audio'))
# v2_api.register(api2.DocketResource(tally_name='search.api2.docket'))
# v2_api.register(api2.CitationResource(tally_name='search.api2.citation'))
# v2_api.register(api2.JurisdictionResource(tally_name='search.api2.court'))
# v2_api.register(api2.DocumentResource(tally_name='search.api2.document'))
# v2_api.register(api2.SearchResource(tally_name='search.api2.search'))
# v2_api.register(api2.CitesResource(tally_name='search.api2.cites'))
# v2_api.register(api2.CitedByResource(tally_name='search.api2.cited-by'))

urlpatterns = [
    # Search pages
    url(r'^$', 'cl.search.views.show_results'),  # the home page!

    # The API
#    url(r'^api/rest/', include(v1_api.urls)),
#    url(r'^api/rest/', include(v2_api.urls)),

    # Feeds & Podcasts
    url(r'^feed/(search)/$', SearchFeed()),
    # lacks URL capturing b/c it will use GET queries.
    url(r'^feed/court/all/$', AllJurisdictionsFeed()),
    url(r'^feed/court/(?P<court>\w{1,15})/$', JurisdictionFeed()),
]