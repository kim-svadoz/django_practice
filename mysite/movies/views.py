from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:index')

    else:
        form = MovieForm()
    context = {
        'form' : form
    }
    return render(request, 'movies/form.html', context)

def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method=="POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:index')
    else:
        form = MovieForm(instance=movie)
    context={
        'form':form
    }
    return render(request, 'movies/form.html', context)

def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context={
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('movies:index')


