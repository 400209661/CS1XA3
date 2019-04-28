from django.shortcuts import render
from .models import Score


def home(request):
    leaderBoard = {
        'scores': Score.objects.all()
    }
    return render(request, 'simon/home.html', leaderBoard)

def about(request):
    return render(request, 'simon/about.html', {'title': 'About'})
