from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.login.urls', namespace="login")),
    url(r'^faves/', include('apps.faves.urls', namespace="faves")),
    url(r'^random/', include('apps.rand.urls', namespace="rand")),
    url(r'^popular/', include('apps.pop.urls', namespace="pop")),
    url(r'^find/', include('apps.find.urls', namespace="find")),
]


    
