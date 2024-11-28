from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request) -> HttpResponse:
    context: dict = {
        'title': 'Home', 
        'content': 'Главная страница - HOME'
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    return render(request, 'main/about.html')
