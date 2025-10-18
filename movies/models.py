from django.db import models

# Create your models here.

class Movie(models.Model):
    STATUS_CHOICES = [
        ('watching', 'Watching'),
        ('completed', 'Completed'),
        ('wishlist', 'Wishlist'),
        ('dropped', 'Dropped'),
    ]

    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    platform = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='wishlist')
    total_episodes = models.IntegerField(default=0)
    watched_episodes = models.IntegerField(default=0)
    rating = models.FloatField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='movie_images/', blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
