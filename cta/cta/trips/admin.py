from django.contrib import admin
from cta.trips.models import Trip


class TripAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'destination_name','route', 'expected_arrival', 'run_number', 'degree')

    pass
admin.site.register(Trip, TripAdmin)
