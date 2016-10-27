from django.conf.urls import url
from . import views
from .views import Index, Find, Results, Reset

urlpatterns = [
	url(r'^$', Index.as_view(), name='index'),
	url(r'^reset$', Reset.as_view(), name='reset'),
	url(r'^(?P<name>\w+)$', Find.as_view(), name='find'),
	url(r'^(?P<name>\w+)/results$', Results.as_view(), name='results'),
]
