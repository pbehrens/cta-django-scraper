from django.contrib import admin
from cta.scraper.models import Stop, Route, CtaTrip, Line

admin.site.register(Stop)
admin.site.register(Route)
admin.site.register(CtaTrip)
admin.site.register(Line)