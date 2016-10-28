from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^newname$', views.newname, name = 'newname'),
    url(r'^(?P<id>[0-9]+)/add$', views.addfav, name = 'addfav'),
    url(r'^(?P<id>[0-9]+)/del$', views.delfav, name = 'delfav'),
    url(r'^(?P<id>[0-9]+)/delnew$', views.delnew, name = 'delnew')
]
