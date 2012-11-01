from piston.handler import BaseHandler
from cta.prediction.models import Prediction

class PredictionHandler(BaseHandler):
   allowed_methods = ('GET',)
   model = Prediction   

   def read(self, request, id):
      base = Prediction.objects
      if id:
         return base.get(pk=id)
      else:
         return base.all() # Or base.filter(...)

