from django.conf.urls import url
from . import views
from .views import Index, Filter

urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^filter$', Filter.as_view(), name="filter"),
]
