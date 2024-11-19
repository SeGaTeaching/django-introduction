from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
 
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        pages = request.POST.get('page_numbers')
        
        Book.objects.create(title=title, author=author,page_number=pages)
        return HttpResponse(f"Title: {title}, Author: {author}, Pages: {pages}")
    
    return render(request, 'book/book.html')