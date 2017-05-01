from django.conf.urls import url

app_name = "bintime"

from . import views

urlpatterns = [
    url(r'^$', views.bintime, name='bintime')
]
