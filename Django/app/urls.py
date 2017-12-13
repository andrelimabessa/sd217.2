from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'teste/$', views.post_list),
	url(r'novo/$', views.NovoJogo),
	# url(r'partida', views.Partida),
	# url(r'principal', views.Principal),

]