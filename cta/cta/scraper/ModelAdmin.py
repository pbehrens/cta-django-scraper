from django.contrib import admin
from cta.scraper.models import Stop

class StopAdmin(admin.ModelAdmin):
    pass
admin.site.register(Stop, StopAdmin)