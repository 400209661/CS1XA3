from django.shortcuts import render

def home(request):
    return render(request, 'simon/home.html')

def about(request):
    return render(request, 'simon/about.html')
