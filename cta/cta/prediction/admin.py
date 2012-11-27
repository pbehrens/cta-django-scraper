from django.contrib import admin
from cta.trips.models import Prediction


class TripAdmin(admin.ModelAdmin):
    list_display = ('stop_id', 'stop_name','prediction_time', 'is_delayed', 'wheelchair_boarding', 'wheelchair_boarding')

    pass
admin.site.register(Prediction)
