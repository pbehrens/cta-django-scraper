from django.conf.urls.defaults import *
from piston.resource import Resource
from cta.api.handlers import PredictionHandler

prediction_resource = Resource(PredictionHandler)


# class CsrfExemptResource( Resource ):
#     def __init__( self, handler, authentication = None ):
#         super( CsrfExemptResource, self ).__init__( handler, authentication )
#         self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

# prediction_resource = CsrfExemptResource( PredictionHandler )


urlpatterns = patterns('',
   url(r'^prediction/(?P<id>\d+)$', prediction_resource),
)