from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def greet(request):
    return HttpResponse('works')

def index(request):
    return render(request, 'index.html')

def heike(request):
    # Benutzerdefinierte Funktion, die nicht serialisierbare Objekte in Strings konvertiert
    def custom_serializer(obj):
        return str(obj)  # Konvertiert nicht-serialisierbare Objekte in Strings

    meta_data = dict(request.META)  # Erstelle eine Kopie von request.META

    details = {
        "Method": request.method,
        "Path": request.path,
        "Query Params": dict(request.GET),
        "Headers": dict(request.headers),
        "Body": request.body.decode("utf-8") if request.body else "No Body",
        "META": meta_data,
    }

    # Serialisiere die Daten mit der benutzerdefinierten Serializer-Funktion
    request_data = json.dumps(details, default=custom_serializer, indent=4)

    return HttpResponse(f"{request.session.items()}<pre>{request_data}</pre>")

def search(request):
    user = request.GET['name']
    age = request.GET['age']
    city = request.GET['city']
    return HttpResponse(f'user ist {user.title()} und {age} Jahre alt und kommt aus {city}')

def show(request):
    scheme = request.scheme
    method = request.method
    address = request.get_host()
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path
    encoding = request.encoding
    session = request.session
    session['task'] = 'do homework'
    
    msg = f"""
    <html>
    <body>
        <h1>Request Information</h1>
        <p>Scheme: {scheme}</p>
        <p>Method: {method}</p>
        <p>Address: {address}</p>
        <p>User Agent: {user_agent}</p>
        <p>Path Info: {path_info}</p>
        <p>Encoding: {encoding}</p>
        <p>Session: {session.items()}</p>
        <p>Headers: {request.headers.items()}</p>     
    </body>
    </html>
    """
    
    return HttpResponse(msg)

def answer(request):
    response = HttpResponse()
    status = response.status_code
    headers = response.headers
    content = response.content
    cookies = response.cookies
    items = response.items()
    status = 201
    
    headers['Age'] = 20
    
    msg = f"""
    <html>
    <body>
        <h1>Response Information</h1>
        <p>Stauts: {status}</p>
        <p>Header: {headers}</p>
        <p>Content: {content}</p>
        <p>Cookies: {cookies}</p>
        <p>Items: {items}</p>   
    </body>
    </html>
    """
    
    return HttpResponse(msg)

def form(request):
    """"
    if request.method == 'GET':
        method = request.method
        return render(request, 'form.html', {'method': method})
    
    elif request.method == 'POST':
        method = request.method
        return render(request, 'form.html', {'method': method})
    """
    method = request.method
    return render(request, 'form.html', {'method': method})

from django.contrib.sessions.models import Session
def get_session_data(session_key):
    try:
        session = Session.objects.get(session_key=session_key)
        data = session.get_decoded()
        return(data)
    except Session.DoesNotExist:
        return 'Session not found.'