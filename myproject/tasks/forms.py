from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'add a task',
                'required': True
            }
        )
    )
    
class AsyncTaskForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'id': 'title-async',
                'placeholder': 'add a task',
                'required': True
            }
        )
    )