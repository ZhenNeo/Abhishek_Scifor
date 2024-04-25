from django.shortcuts import render


def game_board(request):
    return render(request, 'game_board.html')
