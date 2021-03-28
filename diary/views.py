from django.shortcuts import render
from django.http import HttpResponse
from .models import Dairy


def index(request):
    dairies = Dairy.objects.all()
    context = {
        'message': 'Hello my diary',
        'dairies': dairies,
    }
    return render(request, 'diary/index'.html, context)