from django.urls import path
from .views import *

app_name = 'toolss'

urlpatterns = [
    path('', main, name='main'),
    path('detail/<int:pk>', detail, name='detail'),
    path('create/', create, name='create'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
]