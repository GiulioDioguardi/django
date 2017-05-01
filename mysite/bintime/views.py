from django.shortcuts import render

def bintime(request):
    return render(request, 'bintime/bintime.html', {})
