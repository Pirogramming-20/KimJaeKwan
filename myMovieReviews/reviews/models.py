from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=32)
    director = models.CharField(max_length=32)
    mainActor = models.CharField(max_length=32)
    genre = models.CharField(max_length=32)
    horoscope = models.IntegerField()
    runningTime = models.IntegerField()
    reviewContent = models.TextField()