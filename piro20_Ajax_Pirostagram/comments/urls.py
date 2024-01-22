from django.urls import path
from .views import *

app_name = 'comments'

urlpatterns = [
    path('create/<int:pk>', comment_create, name='comment_create'),
]