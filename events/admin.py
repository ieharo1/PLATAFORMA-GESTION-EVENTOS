from django.contrib import admin
from .models import Certificate, Event, EventSpeaker, Flyer, Registration, Speaker

admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(EventSpeaker)
admin.site.register(Flyer)
admin.site.register(Registration)
admin.site.register(Certificate)
