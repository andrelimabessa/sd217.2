from django.conf.urls import include, url
from .views import novo, partida

urlpatterns = [
	url(r'novo/$', novo),
	url(r'partida', partida, name='partida'),
]