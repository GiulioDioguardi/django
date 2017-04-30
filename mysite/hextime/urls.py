from django.conf.urls import url

app_name = "hextime"

from . import views

urlpatterns = [
    url(r'^$', views.hextime, name='hextime')
]