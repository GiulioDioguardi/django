from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def hextime(request):
    return render(request, 'hextime/hextime.html', {})