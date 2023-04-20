from django.contrib import admin
from .models import *
from Registration import models
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    pass

class TicketAdmin(admin.ModelAdmin):
    pass

class OrganizationAdmin(admin.ModelAdmin):
    pass

class ParticipantsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Participants, ParticipantsAdmin)
admin.site.register(models.User)