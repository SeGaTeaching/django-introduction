from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
 
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        pages = request.POST.get('page_numbers')
        genre = request.POST.get('genre')
        published_date = request.POST.get('published_date')
        
        Book.objects.create(title=title, author=author,page_number=pages, genre=genre, published_date=published_date)
        return HttpResponse(f"Title: {title}, Author: {author}, Pages: {pages}")
    
    return render(request, 'book/book.html')

def library_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            genre = form.cleaned_data['genre']
            published_date = form.cleaned_data['published_date']
            page_number = form.cleaned_data['page_number']
            
            book = Book(
                title=title,
                author=author,
                genre=genre,
                published_date= published_date,
                page_number = page_number
            )
            book.save()
            return render(request, "book/library_success.html", {"data": form.cleaned_data})
        else:
            return render(request, 'book/library-form.html', {'form': form})
            
    form = BookForm()
    return render(request, 'book/library-form.html', {'form': form})