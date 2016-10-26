from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<id>[0-9]+)/add$', views.addfav, name = 'addfav'),
    url(r'^(?P<id>[0-9]+)/del$', views.delfav, name = 'delfav')
]
