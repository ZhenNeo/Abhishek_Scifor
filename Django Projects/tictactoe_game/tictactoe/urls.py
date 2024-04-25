from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_board, name='game_board')
]
