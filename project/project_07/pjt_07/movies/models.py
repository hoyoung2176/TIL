from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200)
    
class Movie(models.Model):
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    
class Score(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    content = models.CharField(max_length=200)
    score = models.IntegerField()
    
     