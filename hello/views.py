from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'enemy': 'スライム'
    }
    return render(request, 'hello/index.html', context)
