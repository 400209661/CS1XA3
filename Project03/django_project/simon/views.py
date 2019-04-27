from django.shortcuts import render


scores = [
    {
        'username': 'Alex',
        'score': '99',
        'date_posted': 'April 27 2019'
    },
    {
        'username': 'Jane',
        'score': '100',
        'date_posted': 'August 28 2019'
    }
]

def home(request):
    leaderBoard = {
        'scores': scores
    }
    return render(request, 'simon/home.html', leaderBoard)

def about(request):
    return render(request, 'simon/about.html', {'title': 'About'})
