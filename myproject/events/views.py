from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
from .forms import EventForm

# Create your views here.
def event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('event_success', event_id=event.id)
            #return render(request, 'events/event_success.html', {'form': form.cleaned_data})
        else:
            return render(request, 'events/event_form.html', {'form': form})
    else:
        form = EventForm()
        return render(request, 'events/event_form.html', {'form': form})
    
def event_success(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/event_success.html', {'event': event})