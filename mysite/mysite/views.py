from django.shortcuts import render
from django.conf import settings
import re

def home(request):
    user_apps = []
    for app in settings.INSTALLED_APPS:
        if not 'django' in app:
            user_apps.append(re.sub(r'\..*$', '', app))
    return render(request, 'home.html', {'apps': user_apps})
