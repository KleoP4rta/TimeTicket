from django.contrib import admin
from .models import *
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    pass

class TicketAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Organization)
admin.site.register(Participants)