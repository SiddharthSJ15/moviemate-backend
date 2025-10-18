from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer

@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all().order_by('-created_at')
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_movie(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    except Movie.DoesNotExist:
        return Response({"detail": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_movie(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
    except Movie.DoesNotExist:
        return Response({"detail": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = MovieSerializer(movie, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_movie(request, pk):
    try:
        movie = Movie.objects.get(id=pk)
    except Movie.DoesNotExist:
        return Response({"detail": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
    
    movie.delete()
    return Response({"detail": "Movie deleted"}, status=status.HTTP_204_NO_CONTENT)
