from django.db import models
from posts.models import Post 
# Create your models here.
class Comment(models.Model):
    content = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)