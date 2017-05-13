from . import views
from django.conf.urls import url

app_name = 'itemstore'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(?P<product_id>[0-9]+)/buy/$', views.buy, name='buy'),
    url(r'(?P<product_id>[0-9]+)/restock/$', views.restock, name='restock'),
]
