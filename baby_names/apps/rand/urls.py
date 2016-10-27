from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^randName$', views.randName, name="randName"),
    url(r'^new$', views.new, name="new"),
]
