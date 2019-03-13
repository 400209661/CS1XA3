from django.shortcuts import render
from django.http import HttpResponse

def elm_app(request):
     html = "<html><body>Hello World</body></html>"
     return HttpResponse(html)
