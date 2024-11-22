from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'date_time',
            'location',
            'description',
            'max_participants',
            'category'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Describe the event...'}),
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }