from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'teste/$', views.post_list),
	url(r'teste/Njogo/$', views.NovoJogo),
	url(r'^$', views.NovoJogo),
	url(r'partida', views.Partida),
	url(r'principal', views.Principal),

]
