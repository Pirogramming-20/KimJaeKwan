from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=24)
    content = models.TextField()
    like = models.BooleanField()