from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^register$', views.register, name = 'register'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^loginRegistration$', views.index, name = 'loginRegistration'),
    url(r'^logout$', views.logout, name = 'logout'),

]