from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, name):
    return HttpResponse(f'Hello {name.title()} my friend, welcome')

def walter(request):
    return HttpResponse('Hello Walter!')

def math(request, num1, num2):
    add = float(num1) * float(num2)
    return HttpResponse(f'Das Ergebnis von {num1} * {num2} ist {add}')
