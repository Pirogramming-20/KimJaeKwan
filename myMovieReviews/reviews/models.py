from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=32)
    director = models.CharField(max_length=32)
    mainActor = models.CharField(max_length=32)
    GENRE_CHOICES = [
        ('action', '액션'),
        ('comedy', '코미디'),
        ('drama', '드라마'),
        ('sf', 'SF'),
        ('horror', '공포'),
    ]
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES)
    horoscope = models.IntegerField()
    runningTime = models.IntegerField()
    reviewContent = models.TextField()