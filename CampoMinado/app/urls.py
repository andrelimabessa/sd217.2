from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'teste/$', views.post_list),
	url(r'^$', views.campo),		
]