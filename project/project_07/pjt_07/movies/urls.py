from django.urls import path,include
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:movies_pk>/scores/<int:score_pk>/delete', views.scores_delete, name = 'scores_delete'),
    path('<int:movies_pk>/scores/new', views.scores_create, name = 'scores_create'),
    path('<int:movies_pk>/delete/', views.delete, name = 'delete'),
    path('<int:movies_pk>/', views.detail, name = 'detail'),
    path('', views.index, name='index'),
]