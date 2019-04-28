from django.shortcuts import render
from .models import Score
from django.contrib.auth.decorators import login_required

def home(request):
    leaderBoard = {
        'scores': Score.objects.all()
    }
    return render(request, 'simon/home.html', leaderBoard)

@login_required
def about(request):
    return render(request, 'simon/about.html', {'title': 'About'})
