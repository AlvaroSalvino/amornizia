from django.urls import path
from .views import *

urlpatterns = [
    path('home/', index, name='index'),
    path('presentes/', presentes, name='presentes'),
    path('carta/', carta, name='carta'),
    path('meu_coracao/', meu_coracao, name='meu_coracao'),
    path('snape/', snape, name='snape'),
]