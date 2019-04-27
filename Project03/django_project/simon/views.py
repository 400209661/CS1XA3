from django.shortcuts import render


scores = [
    {
        'username': 'Alex',
        'score': '101',
        'date_posted': 'August 27 2018'
    },
    {
        'username': 'Jane',
        'score': '100',
        'date_posted': 'August 28 2018'
    }
]

def home(request):
    context = {
        'scores': scores
    }
    return render(request, 'simon/home.html', context)

def about(request):
    return render(request, 'simon/about.html')
