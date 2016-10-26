from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^find$', find, name='find')
]
