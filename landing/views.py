from django.shortcuts import render
from events.models import Event
from django.http import HttpResponse

# Create your views here.
def index(request):
    events  = Event.objects.get()
    args    = {'events':events} 
    return render(request,'index.html',args)


def test(request):
    events = Event.objects.get()
    return HttpResponse(events.vanue)