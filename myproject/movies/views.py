from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import MovieForm

# Create your views here.
@login_required(login_url='accounts:login')
def watchlist_view(request):
    movies = Movie.objects.filter(user=request.user)
    return render(request, 'movies/movies.html', {'movies': movies})

@login_required(login_url='accounts:login')
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:watchlist')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})