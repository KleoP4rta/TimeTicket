from django.shortcuts import render
from django.utils import timezone
from django.db.models.functions import Lower
from .models import *
from . import *


def main(request):
    events = Event.objects.all()
    now = timezone.now()
    context = {
        'now': now,
        'events': events
    }
    return render(request, 'main.html', context)


def time(event_date):
    now = timezone.now()
    time_left = event_date - now
    days_left = time_left.days
    hours_left = time_left.seconds // 3600
    minutes_left = (time_left.seconds // 60) % 60
    time = f'{days_left}, {hours_left}, {minutes_left}'
    return time
##############################################################
# вывод всех мероприятий продавца
def organizer(request):
    context = {
        'events': Event.objects.filter(author=request.user)
    }
    return render(request, '.html', context)

# вывод всех билетов покупателя
def tickets(request):
    context = {
        'events': Ticket.objects.filter(author=request.user)
    }
    return render(request, '.html', context)

def create(request):
    return render(request, '.html')

