from django.shortcuts import render
from .models import Score
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

def home(request):
    leaderBoard = {
        'scores': Score.objects.all()
    }
    return render(request, 'simon/home.html', leaderBoard)

class ScoreListView(ListView):
    model = Score
    template_name = 'simon/home.html'
    context_object_name = 'scores'
    ordering = ['-date_posted']

@login_required
def about(request):
    return render(request, 'simon/about.html', {'title': 'Game'})
