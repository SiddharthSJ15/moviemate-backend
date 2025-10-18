from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_movies, name='get_movies'),
    path('movies/add/', views.add_movie, name='add_movie'),
    path('movies/<int:pk>/', views.get_movie, name='get_movie'),
    path('movies/<int:pk>/update/', views.update_movie, name='update_movie'),
    path('movies/<int:pk>/delete/', views.delete_movie, name='delete_movie'),
]
