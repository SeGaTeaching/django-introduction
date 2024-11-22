from django.shortcuts import render
from django.http import HttpResponse
from .forms import PizzaOrderForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            size = form.cleaned_data['size']
            date = form.cleaned_data['date']
            
            response_message = f"""
                <h1>Order Received!</h1>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Pizza Size:</strong> {size}</p>
                <p><strong>Date</strong> {date}</p>
            """
            return HttpResponse(response_message)
        else: 
            form = PizzaOrderForm()
    form = PizzaOrderForm()        
    return render(request, 'django_forms/index.html', {'form': form})