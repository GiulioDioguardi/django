from . import views
from django.conf.urls import url

app_name = 'itemstore'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
