from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Movie, Genre, Score
# Create your views here.
def index(request):
    # movies = Movie.objects.order_by('-pk')
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).all() #score 컬럼에 __ score table
    
    
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)

def detail(request, movies_pk):
    movies = Movie.objects.annotate(score_avg=Avg('score__score')).get(pk=movies_pk)
    # movies = Movie.objects.get(pk=movies_pk)
    scores = movies.score_set.all()
    genre = Genre.objects.get(pk=movies.genre_id)
    context = {
        'movies' : movies,
        'scores' : scores,
        'genre' : genre,
    }
    
    return render(request, 'movies/detail.html/', context)

def delete(request, movies_pk):
    movies = Movie.objects.get(pk=movies_pk)
    movies.delete()
    return redirect('/movies/')
    
def scores_create(request, movies_pk):
    movie = Movie.objects.get(pk=movies_pk)
    content = request.POST.get('content')
    score = request.POST.get('score')
    scores = Score(movie = movie, content= content, score=score)
    scores.save()
    return redirect('movies:detail', movies_pk)
    
def scores_delete(request, movies_pk, score_pk):
    movie = Movie.objects.get(pk=movies_pk)
    scores = Score.objects.get(pk=score_pk)
    scores.delete()
    return redirect('movies:detail', movies_pk)
    
    